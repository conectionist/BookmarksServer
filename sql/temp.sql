select *
from links;

select *
from users;

select *
from tags;

select l.link, t.nume
from links l, users u, tags t
where u.nume='dan';

select *
from userlinks;

insert into userlinks
values(4,1);

insert into UserLinks
values(13,11);

select parola
from users
where nume='ionica';

delete from userlinks where user_id=1;

SELECT parola
            FROM users
            WHERE nume = 'ionica';delete from userlinks where user_id=1;-- '

select *
from userlinks;

insert into users(nume,parola)
values('dan', 'parola');

insert into users(nume,parola)
values('andy', 'muidibat');

select l.link, l.title
from userlinks ul, links l
where ul.user_id = (select id from users where nume = 'dan')
and ul.link_id = l.id;

call save_link('http://9gag.com/gag/aMGDBLG', 'boing boing');

call save_link2('ionica', 'parola\'; delete from users where 1=1 -- ');

select get_password_for_user('dan') as 'password';

select get_user_id('dan1');

call create_user_link('dan', 'http://9gag.com/gag/aMGDBLG');

call create_link_tag_association('http://9gag.com/gag/aMGDBLG', 'bla bla');