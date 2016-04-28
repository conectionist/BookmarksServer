drop procedure if exists save_link;
drop procedure if exists save_tag;
drop procedure if exists save_user;
drop function if exists get_user_id;
drop function if exists get_link_id;
drop function if exists get_tag_id;
drop procedure if exists create_user_link;
drop procedure if exists create_link_tag_association;
drop function if exists get_user_password;
drop procedure if exists get_user_bookmarks;
drop function if exists get_link_tags;

delimiter $$

CREATE PROCEDURE save_link (in p_link varchar(512),
							in p_title varchar(256))
BEGIN
	insert into links(link, title) 
	values (p_link, p_title);
END $$

CREATE PROCEDURE save_tag (in p_name varchar(30))
BEGIN
	insert into tags(nume) 
	values (p_name);
END $$

CREATE PROCEDURE save_user (in p_name varchar(30),
							in p_password varchar(32))
BEGIN
	insert into users(nume, parola) 
	values (p_name,p_password);
END $$

CREATE FUNCTION get_user_id (p_username varchar(30))
	returns int
BEGIN
	declare user_id int;
    
	select id
	into user_id
	from users
	where nume = p_username;
   
   return user_id;
END $$

CREATE FUNCTION get_link_id (p_link varchar(512))
	returns int
BEGIN
	declare link_id int;
    
	select id
	into link_id
	from links
	where link = p_link;
   
   return link_id;
END $$

CREATE FUNCTION get_tag_id (p_tag varchar(30))
	returns int
BEGIN
	declare tag_id int;
    
	select id
	into tag_id
	from tags
	where nume = p_tag;
   
   return tag_id;
END $$

CREATE PROCEDURE create_user_link (in p_username varchar(30),
							       in p_link varchar(512))
BEGIN
	declare user_id int;
    declare link_id int;
    
    select get_user_id(p_username) into user_id;
    
	IF(user_id is null) THEN 
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'You must accept the truth. There us no username!';
	END IF;
    
    select get_link_id(p_link) into link_id;
    
    IF(link_id is null) THEN 
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'You must accept the truth. There us no link!';
	END IF;
    
    insert into userlinks
    values(link_id, user_id);
END $$

CREATE PROCEDURE create_link_tag_association (in p_link varchar(512),
							                  in p_tag varchar(30))
BEGIN
	declare tag_id int;
    declare link_id int;
    
    select get_tag_id(p_tag) into tag_id;
    
	IF(tag_id is null) THEN 
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'You must accept the truth. There us no tag!';
	END IF;
    
    select get_link_id(p_link) into link_id;
    
    IF(link_id is null) THEN 
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'You must accept the truth. There us no link!';
	END IF;
    
    insert into linkstagassociation
    values(link_id, tag_id);
END $$

CREATE FUNCTION get_user_password (p_username varchar(30))
	returns varchar(32)
BEGIN
	declare passwd varchar(32) default '';
    
   select parola
   into passwd
   from users
   where nume = p_username;
   
   return passwd;
END $$

CREATE procedure get_user_bookmarks (p_username varchar(30))
BEGIN
	-- declare v_link varchar(512) default '';

	select link
	-- into v_link
	from links;
	-- where nume = p_username;

	-- return v_link;
END $$

CREATE FUNCTION get_link_tags (p_link varchar(512))
	returns varchar(32)
BEGIN
	declare passwd varchar(32) default '';
    
   select parola
   into passwd
   from users
   where nume = p_username;
   
   return passwd;
END $$

delimiter ;

commit;