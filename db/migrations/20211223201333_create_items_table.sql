-- migrate:up
CREATE TABLE item
(
  id           integer generated always as identity PRIMARY KEY,
  title text      not null,
  description text,
  created_at   timestamp not null DEFAULT CURRENT_TIMESTAMP,
  updated_at   timestamp
);

-- migrate:down
DROP TABLE item;
