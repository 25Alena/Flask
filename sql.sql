create table  if not exists comands (
id integer primary key autoincrement,
name_of_comand text not null,
achivements text not null,
sostav text not null,
identif text not null,
time integer not null
);

create table  if not exists users (
id integer primary key autoincrement,
login text not null,
psw text not null
);