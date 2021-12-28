CREATE VIEW COUNTRY_COUNT AS
select country, count(country)
	from players
	left join colleges on players.p_college = colleges.p_college
	group by country