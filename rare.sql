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


INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');


DELETE FROM Users WHERE id = 1;

INSERT INTO Posts VALUES (null, 1, 2, "some content", '2021-10-25', "http://", "look at this", 1 );

SELECT * FROM Posts

SELECT * FROM Users


SELECT * FROM Posts;

INSERT INTO Users VALUES (1, "Danny", "Armstrong", "danny@danny.com", "I am Danny", "danny@danny.com", "123", "http://", "2021-10-26", 1)
SELECT * FROM Users;


INSERT INTO Posts 
VALUES (null, 1, 2, "some content", '2021-10-25', "http://", "look at this", 1 );

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

DELETE FROM Posts
WHERE id > 0;

SELECT
p.id,
p.user_id,
p.title,
p.publication_date,
p.image_url,
p.content,
p.approved,
u.id u_id,
u.first_name,
u.last_name,
c.id cat_id,
c.label
FROM Posts p
JOIN users u on p.user_id = u_id
left JOIN categories c on p.category_id = c.id
ORDER BY publication_date desc;

SELECT * FROM postTags;

SELECT pt.id pt_id,
        pt.post_id,
        pt.tag_id,
        t.id t_id,
        t.label
        FROM postTags pt
        JOIN Tags t on t_id = pt.tag_id;

ALTER TABLE Comments 
ADD created_on date;

SELECT p.id p_id,
        p.user_id,
        p.category_id,
        p.title,
        p.publication_date,
        p.image_url,
        p.content,
        p.approved,
        u.id u_id,
        u.first_name,
        u.last_name,
        c.id c_id,
        c.post_id c_postId,
        c.author_id,
        c.content c_content,
        c.created_on
        FROM Posts p
        JOIN Users u ON u_id = p.user_id
        LEFT JOIN Comments c ON c_postId = p.id
        WHERE p_id = 44;

SELECT * from tags;

SELECT pt.id pt_id,
        pt.post_id,
        pt.tag_id,
        t.id t_id,
        t.label
        FROM postTags pt
        JOIN Tags t on t_id = pt.tag_id
    

ALTER TABLE Users
ADD is_staff bit;

select * from Posts
where approved = 0 or approved = 1;

UPDATE Users
SET is_staff = 0;

UPDATE Users
SET is_staff = 1
WHERE id = 1;


SELECT 
pt.id,
pt.post_id,
pt.tag_id
FROM PostTags pt
Where post_id = 40;