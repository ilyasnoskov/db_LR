-- хто більше і хто менше 2 метрів
select count(p_height) from height where p_height >= 200 -- more 2 meters
select count(p_height) from height where p_height < 200

-- відсоток гравців кожної країни
Select country, count(country)
	from players
	left join colleges on players.p_college = colleges.college
	group by country

-- кількість гравців із певного коледжу
select p_college, count(p_college) from players
	group by p_college