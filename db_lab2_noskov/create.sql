DROP table if exists players CASCADE;
DROP table if exists colleges CASCADE;
DROP table if exists height CASCADE;

create table players (
  p_id int primary key not null ,
  p_name char(256) not null,
  p_college char(256) not null
);

create table colleges(
  p_college char(256) primary key not null,
  country char(256) not null
);

create table height(
	p_id int not null,
	p_height int not null
);

alter table  height add constraint FK_height_player foreign key (p_id) references players (p_id);
alter table  players add constraint FK_college_country foreign key (p_college) references colleges (p_college);