CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    nickname VARCHAR(255),
    email VARCHAR(255),
    money: FLOAT
);

COMMENT ON TABLE users IS 'Информация о пользователях';

COMMENT ON TABLE users.user_id IS 'Уникальный идентификатор пользователя';

COMMENT ON COLUMN users.nickname IS 'Имя пользователя';

COMMENT ON COLUMN users.email IS 'Email пользователя';

COMMENT ON COLUMN users.money IS 'Количество денег на счету пользователя';

CREATE TABLE developers(
    developer_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    website VARCHAR(255),
    country VARCHAR(50)
);

COMMENT ON TABLE developers IS 'Информация о разработчиках';

COMMENT ON COLUMN developers.developer_id IS 'Уникальный идентификатор разработчика';

COMMENT ON COLUMN developers.name IS 'Название компании-разработчика';

COMMENT ON COLUMN developers.website IS 'Сайт разработчика';

COMMENT ON COLUMN developers.country IS 'Страна регистрации разработчика';

CREATE TABLE games(
    game_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    developer_id INT REFERENCES developers(developer_id) ON DELETE CASCADE,
    rating FLOAT,
    price FLOAT,
    release_date DATE,
    version VARCHAR(20),
    description VARCHAR(600)
);

COMMENT ON TABLE games IS 'Таблица игр';

COMMENT ON COLUMN games.game_id IS 'Уникальный идентификатор игры';

COMMENT ON COLUMN games.release_date IS 'Дата выхода';

COMMENT ON COLUMN games.developer_id IS 'Идентификатор разработчика';

COMMENT ON COLUMN games.rating IS 'Рейтинг игры';

COMMENT ON COLUMN games.price IS 'Цена игры';

COMMENT ON COLUMN games.name IS 'Название игры';

COMMENT ON COLUMN games.version IS 'Версия игры';

COMMENT ON COLUMN games.description IS 'Описание игры';

CREATE TABLE user_games(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    game_id INT REFERENCES games(game_id) ON DELETE CASCADE,
    rating FLOAT
);

COMMENT ON TABLE user_games IS 'Таблица связи пользователей и игр';

COMMENT ON COLUMN user_games.id IS 'Уникальный идентификатор записи'; 

COMMENT ON COLUMN user_games.user_id IS 'Идентификатор пользователя';

COMMENT ON COLUMN user_games.game_id IS 'Идентификатор игры';

COMMENT ON COLUMN user_games.rating IS 'Оценка игры пользователем';

CREATE TABLE achievements(
    achievement_id SERIAL PRIMARY KEY,
    game_id INT REFERENCES games(game_id) ON DELETE CASCADE,
    name VARCHAR(100),
    description VARCHAR(255)
)

COMMENT ON TABLE achievements IS 'Таблица достижений';

COMMENT ON COLUMN achievements.achievement_id IS 'Уникальный идентификатор достижения';

COMMENT ON COLUMN achievements.game_id IS 'Идентификатор игры';

COMMENT ON COLUMN achievements.name IS 'Название достижения';

COMMENT ON COLUMN achievements.description IS 'Описание достижения';

CREATE TABLE user_achievement(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    achievement_id INT REFERENCES achievements(achievement_id) ON DELETE CASCADE,
    receive_date DATE
)

COMMENT ON TABLE user_achievement IS 'Таблица достижений пользователей';

COMMENT ON COLUMN user_achievement.id IS 'Уникальный идентификатор';

COMMENT ON COLUMN user_achievement.user_id IS 'Идентификатор пользователя';

COMMENT ON COLUMN user_achievement.achievement_id IS 'Идентификатор достижения';

COMMENT ON COLUMN user_achievement.receive_date IS 'Дата получения достижения';

CREATE TABLE friendship(
    friendship_id SERIAL PRIMARY KEY,
    user_id1 INT REFERENCES users(user_id) ON DELETE CASCADE,
    user_id2 INT REFERENCES users(user_id) ON DELETE CASCADE,
    status ENUM ('requested', 'accepted')
)

COMMENT ON TABLE friendship IS 'Таблица отношений между пользователями';

COMMENT ON COLUMN friendship.friendship_id IS 'Уникальный идентификатор отношений';

COMMENT ON COLUMN friendship.user_id1 IS 'Идентификатор первого пользователя из пары';

COMMENT ON COLUMN friendship.user_id2 IS 'Идентификатор второго пользователя из пары';

COMMENT ON COLUMN friendship.status IS 'Статус отношений';