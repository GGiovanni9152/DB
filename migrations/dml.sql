INSERT INTO 
    users (nickname, password, email, money)
VALUES
    (
        'GGiovanni',
        '123',
        'ggiovanni@gmail.com',
        100.0
    ),
    (
        'Motya',
        '123',
        'begemotya@gmail.com',
        80.0
    ),
    (
        'Romania666',
        '123',
        'roman@gmail.com',
        75.0
    ),
    (
        'Maksimka',
        '123',
        'Maksimka@yandex.com',
        90
    );

INSERT INTO
    admins(user_id)
VALUES
    (
        1
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
    ),
    (
        'Paradox Interactive',
        'Paradox.com',
        'Sweden'
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
        'Hearts of Iron IV',
        100
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
        2,
        'Real PATRIOT',
        'Complete Smyta'
    ),
    (
        3,
        'No more girls',
        'Start playing Hearts of Iron IV'
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
    game_detail(game_id, developer_id, rating, release_date, version, description, picture_name)
VALUES
    (
        1,
        1,
        3.5,
        '2013-06-03',
        '7.37d',
        'Every day, millions of players worldwide enter battle as one of over a hundred Dota heroes. And no matter if its their 10th hour of play or 1,000th, theres always something new to discover. With regular updates that ensure a constant evolution of gameplay, features, and heroes, Dota 2 has taken on a life of its own.',
        'Dota.jpg'
    ),
    (
        2,
        3,
        2,
        '2024-05-16',
        '1.3',
        'The plot unfolds in 1612, during the Time of Troubles. In the Russian kingdom - famine, wars, Polish intervention, impostors trying to take the throne. The main character of the game is a young boyar Yuri Miloslavsky. In order to save his beloved, he swore allegiance to the Polish queen Vladislav IV, but still in time became a participant of the popular uprising against the invaders.',
        'Smyta.jpg'
    ),
    (
        3,
        4,
        8,
        '2016-03-11',
        '1.72',
        'Victory is at your fingertips! Your ability to lead your nation is your supreme weapon, the strategy game Hearts of Iron IV lets you take command of any nation in World War II; the most engaging conflict in world history.',
        'Heartsofiron.jpg'
    );
