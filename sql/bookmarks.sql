use bookmarks;

drop table if exists UserLinks;
drop table if exists LinksTagAssociation;
drop table if exists users;
drop table if exists tags;
drop table if exists links;

-- the "links" table
create table links
(
	id int PRIMARY KEY AUTO_INCREMENT,
	link varchar(512) NOT NULL,
    title varchar(256) NOT NULL,
    UNIQUE(link)
);

-- the "tags" table
create table tags
(
	id int PRIMARY KEY AUTO_INCREMENT,
	nume varchar(30) NOT NULL,
    UNIQUE(nume)
);

-- the "users" table
create table users
(
	id int PRIMARY KEY AUTO_INCREMENT,
	nume varchar(30) NOT NULL,
    parola varchar(32) NOT NULL,
    UNIQUE(nume)
);

-- the "LinksTagAssociation" table
create table LinksTagAssociation
(
	link_id int NOT NULL,
	tag_id int NOT NULL,
	FOREIGN KEY (link_id) REFERENCES links(id),
	FOREIGN KEY (tag_id) REFERENCES tags(id),
    PRIMARY KEY (link_id, tag_id)
);

-- the "UserLinks" table
create table UserLinks
(
	link_id int NOT NULL,
	user_id int NOT NULL,
	FOREIGN KEY (link_id) REFERENCES links(id),
	FOREIGN KEY (user_id) REFERENCES users(id),
    PRIMARY KEY (link_id, user_id)
);
