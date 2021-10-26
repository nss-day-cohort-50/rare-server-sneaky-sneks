CREATE TABLE "Users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "first_name" varchar,
    "last_name" varchar,
    "email" varchar,
    "bio" varchar,
    "username" varchar,
    "password" varchar,
    "profile_image_url" varchar,
    "created_on" date,
    "active" bit
);
CREATE TABLE "DemotionQueue" (
    "action" varchar,
    "admin_id" INTEGER,
    "approver_one_id" INTEGER,
    FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
    FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
    PRIMARY KEY (action, admin_id, approver_one_id)
);
CREATE TABLE "Subscriptions" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "follower_id" INTEGER,
    "author_id" INTEGER,
    "created_on" date,
    FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
    FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE "Posts" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER,
    "category_id" INTEGER,
    "title" varchar,
    "publication_date" date,
    "image_url" varchar,
    "content" varchar,
    "approved" bit
);
CREATE TABLE "Comments" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "post_id" INTEGER,
    "author_id" INTEGER,
    "content" varchar,
    FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
    FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE "Reactions" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "label" varchar,
    "image_url" varchar
);
CREATE TABLE "PostReactions" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER,
    "reaction_id" INTEGER,
    "post_id" INTEGER,
    FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
    FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
    FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);
CREATE TABLE "Tags" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "label" varchar
);
CREATE TABLE "PostTags" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "post_id" INTEGER,
    "tag_id" INTEGER,
    FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
    FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);
CREATE TABLE "Categories" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "label" varchar
);
<<<<<<< HEAD

INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');


DELETE FROM Users WHERE id = 1;

INSERT INTO Posts VALUES (null, 1, 2, "some content", '2021-10-25', "http://", "look at this", 1 );

SELECT * FROM Posts

SELECT * FROM Users

<<<<<<< HEAD
SELECT * FROM Posts;
=======
INSERT INTO Users VALUES (1, "Danny", "Armstrong", "danny@danny.com", "I am Danny", "danny@danny.com", "123", "http://", "2021-10-26", 1)
SELECT * FROM Users;
>>>>>>> 374d6c8c8723c8fcb46192c679d8f672559c43fb

INSERT INTO Posts 
VALUES (null, 1, 2, "some content", '2021-10-25', "http://", "look at this", 1 );

=======
INSERT INTO Categories ('label')
VALUES ('News');
INSERT INTO Categories ('label')
VALUES ('Sports');
INSERT INTO Categories ('label')
VALUES ('Fiction');
INSERT INTO Categories ('label')
VALUES ('Biography');
INSERT INTO Tags ('label')
VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url')
VALUES ('happy', 'https://pngtree.com/so/happy');
INSERT INTO Categories ('label')
VALUES ('News');
INSERT INTO Tags ('label')
VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url')
VALUES ('happy', 'https://pngtree.com/so/happy');
DELETE FROM Users
WHERE id = 1;
INSERT INTO Posts
VALUES (
        null,
        1,
        2,
        "some content",
        '2021-10-25',
        "http://",
        "look at this",
        1
    );
SELECT *
FROM Posts
SELECT *
FROM Users
INSERT INTO Users
VALUES (
        1,
        "Danny",
        "Armstrong",
        "danny@danny.com",
        "I am Danny",
        "danny@danny.com",
        "123",
        "http://",
        "2021-10-26",
        1
    )
SELECT *
FROM Users;
INSERT INTO Posts
VALUES (
        null,
        1,
        2,
        "some content",
        '2021-10-25',
        "http://",
        "look at this",
        1
    );
    
>>>>>>> 08ac0cdf4cba20c3c96ec6db887ec1801ac176b6
SELECT p.id,
    p.user_id,
    p.category_id,
    p.title,
    p.publication_date,
    p.image_url,
    p.content,
    p.approved,
    u.first_name,
    u.last_name
FROM Posts p
    JOIN Users u ON u.id = p.user_id
WHERE p.user_id = 1;

SELECT *
FROM Categories;

DELETE FROM Categories
WHERE id > 4;