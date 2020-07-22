create table curel(
    ID bigint,
    tweet_id bigint, ---parse from id_str---
    name_id varchar(20), ---screen_name---
    tweet_contents varchar(500), ---text---
    tweet_profile varchar(200), ---desctription---
    follower int,---followers_count---
    tweet_time timestamp,---parse from created_at---
    quoted boolean,---parse from url---
    retweet_count int,---parse from media---
    favorite_count int,---favorite_count---
    mention boolean---parse from usermention---
);