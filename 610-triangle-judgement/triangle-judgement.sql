# Write your MySQL query statement below
-- Select *, if (x+y >z and x +z >y and y+z>x, 'Yes', 'No') as triangle from Triangle

select *, case when (x + y)>z and (x+z)>y and(y+z)>x then 'Yes' else 'No' end as triangle from Triangle