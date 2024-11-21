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
    games(name, developer_id, price, release_date, version)
VALUES
    (
        'Dota2',
        1,
        0,
        09.07.2013,
        '7.37d'
    ),
    (
        'Smyta',
        3,
        50,
        04.04.2024,
        '1.3'
    ),
    (
        'SaintsRow4',
        2,
        30,
        12.08.2015,
        '1.5'
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
        1
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
        03.05.2016
    ),
    (
        2,
        1,
        03.05.2016
    ),
    (
        3,
        1,
        10.08.2019
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
        'accepted',
    ),
    (
        3,
        1,
        'accepted'
    );
