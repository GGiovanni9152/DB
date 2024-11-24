INSERT INTO 
    users (nickname, email, money)
VALUES
    (
        'GGiovanni',
        'ggiovanni@gmail.com',
        100.0
    ),
    (
        'Motya',
        'begemotya@gmail.com',
        80.0
    ),
    (
        'Romania666',
        'roman@gmail.com',
        75.0
    ),
    (
        'Maksimka',
        'Maksimka@yandex.com',
        90
    );

INSERT INTO
    developers (name, website, country)
VALUES
    (
        'Valve',
        'Valve.com',
        'USA'
    ),
    (
        'TBQ',
        'TBQ.com',
        'France'
    ),
    (
        'CyberiaNova',
        'CyberiaNova.ru',
        'Russia'
    );

INSERT INTO
    games(name, price)
VALUES
    (
        'Dota2',
        0
    ),
    (
        'Smyta',
        80
    ),
    (
        'SaintsRow4',
        40
    );

INSERT INTO
    user_games(user_id, game_id, rating)
VALUES
    (
        1,
        1,
        1.0
    ),
    (
        2,
        1,
        5.0
    ),
    (
        3,
        1,
        4.5
    );

INSERT INTO
    achievements(game_id, name, description)
VALUES
    (
        1,
        'Humanity lost',
        'Start playing dota2'
    ),
    (
        3,
        'Real PATRIOT',
        'Complete Smyta'
    );

INSERT INTO
    user_achievement(user_id, achievement_id, receive_date)
VALUES
    (
        1,
        1,
        '2016-06-03'
    ),
    (
        2,
        1,
        '2016-05-03'
    ),
    (
        3,
        1,
        '2019-08-10'
    );

INSERT INTO
    friendship (user_id1, user_id2, status)
VALUES
    (
        1,
        2,
        'accepted'
    ),
    (
        1,
        3,
        'accepted'
    ),
    (
        2,
        1,
        'accepted'
    ),
    (
        3,
        1,
        'accepted'
    );

INSERT INTO 
    game_detail(game_id, developer_id, rating, release_date, version, description)
VALUES
    (
        1,
        1,
        3.5,
        '2013-06-03',
        '7.37d',
        'Every day, millions of players worldwide enter battle as one of over a hundred Dota heroes. And no matter if its their 10th hour of play or 1,000th, theres always something new to discover. With regular updates that ensure a constant evolution of gameplay, features, and heroes, Dota 2 has taken on a life of its own.'
    );
