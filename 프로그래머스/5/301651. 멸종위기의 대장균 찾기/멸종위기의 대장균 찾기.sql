/*with recursive gentree as
    (select id, parent_id, 1 as generation
        from ecoli_data
        where parent_id is null
union all
    select nxtgen.id, nxtgen.parent_id, generation+1
        from ecoli_data nxtgen
        join gentree on nxtgen.parent_id = gentree.id)

select count(parent.id) as count, parent.generation
from gentree parent
left join gentree child on parent.id=child.parent_id
where child.generation is null
group by generation
order by generation asc;*/











-- 재귀함수 사용
-- 1) 1세대 개체 찾기 2) 이를 이용해 모든 세대 개체 분류하기
with recursive gentree as
-- 1세대 
    (select id, parent_id, 1 as generation
        from ecoli_data
        where parent_id is null
    union all
-- 1세대 데이터를 이용해 다음 세대 개체 찾기
     select nextgen.id, nextgen.parent_id, generation+1
        from ecoli_data as nextgen
        join gentree on nextgen.parent_id = gentree.id)
select count(parent.id) as count, parent.generation
from gentree parent
left join gentree child on parent.id=child.parent_id
where child.id is null
group by parent.generation
order by parent.generation asc;