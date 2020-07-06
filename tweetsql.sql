create table tweet_search(
    tweet_id bigint, ---parse from id_str---
    name_id varchar(20), ---screen_name---
    tweet_contents varchar(150), ---text---
    tweet_profile varchar(200), ---desctription---
    follower int,---followers_count---
    tweet_time timestamp,---parse from created_at---
    quoted boolean,---parse from url---
    retweet_count int,---parse from media---
    favorite_count int,---favorite_count---
    mention boolean---parse from usermention---
);