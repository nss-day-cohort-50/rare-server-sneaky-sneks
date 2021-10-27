import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from models import post
from posts.request import delete_post
from users import get_all_users, create_user
from categories import get_all_categories, create_category, update_category, delete_category
from posts import get_all_posts, create_post, get_posts_by_user, get_post_by_id, delete_post

# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.

class HandleRequests(BaseHTTPRequestHandler):
    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    # Here's a class function
    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # http://localhost:8088/entries?q=${searchTerm}
        if '?' in resource:
            param = resource.split('?')[1] # q=${searchTerm}
            resource = resource.split('?')[0]
            term = param.split('=')[1]
            return (resource, id, term)

        else:

            # Try to get the item at index 2
            try:
                # Convert the string "1" to the integer 1
                # This is the new parseInt()
                id = int(path_params[2])
            except IndexError:
                pass
            except ValueError:
                pass

            return (resource, id)

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.

    def do_GET(self):
        """Getter function"""
        self._set_headers(200)
        response = {}  # Default response
        parsed = self.parse_url(self.path)
        
        # Parse the URL and capture the tuple that is returned
        if len(parsed) == 2:
            ( resource, id ) = parsed
            if resource == "users":
                response = f"{get_all_users()}"
            elif resource == "myposts":
                response = f'{get_posts_by_user(id)}'
            elif resource == "post":
                response = f'{get_post_by_id(id)}'
            elif resource == "posts":
                response = f'{get_all_posts()}'
            elif resource == "categories":
                response = f'{get_all_categories()}'
            elif resource == "post":
                response = f'{get_post_by_id(id)}'
        # elif len(parsed) == 3:
        #     ( resource, id, postId ) = parsed
        #     if resource == 'posts':
        #         response = get_post_by_id(postId)
        
        self.wfile.write(response.encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        '''Posts'''
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new...
        new_response = None

        if resource == "posts":
            new_response = create_post(post_body)
        if resource == "register":
            new_response = create_user(post_body)
        elif resource == "categories":
            new_response = create_category(post_body)

        self.wfile.write(f"{new_response}".encode())
        # Encode the new dict and send in response

    # Here's a method on the class that overrides the parent's method.
    # It handles any PUT request.

    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        if resource == "categories":
            was_updated = update_category(id, post_body)
            if was_updated:
                self._set_headers(204)
            else:
                self._set_headers(404)

        # self.wfile.write("".encode())

    def do_DELETE(self):
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL or unpack the tuple
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "categories":
            delete_category(id)
        elif resource == "posts":
            delete_post(id)

        # Encode the new animal and send in response
        self.wfile.write("".encode())


# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
