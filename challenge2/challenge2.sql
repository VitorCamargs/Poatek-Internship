-- 2
select "_CustomerID",sum("Order Quantity"*"Unit Price") USD_spended
from sales_order
group by "_CustomerID"
order by sum("Order Quantity"*"Unit Price") desc
limit 5;

--2.2
select "State",sum("Order Quantity") Units_Sold
from store_locations join sales_order so on store_locations."_StoreID" = so."_StoreID"
group by "State"
order by sum("Order Quantity") desc
limit 1;

--2.3
select "City Name",sum("Order Quantity") total_units_sold
from store_locations join sales_order so on store_locations."_StoreID" = so."_StoreID"
where "State" = 'Indiana'
group by "City Name"
order by total_units_sold desc
limit 1;

--2.4
select "City Name", "Population",
       sum("Order Quantity"*"Unit Price") USD_spended,
       (sum("Order Quantity"*"Unit Price"))/"Population" perCapta
from store_locations join sales_order so on store_locations."_StoreID" = so."_StoreID"
group by "City Name","State","Population" -- Different states can have cities with the same name
order by perCapta desc
limit 1;

--2.5
select "Product Name", sum("Order Quantity") total_units_sold
from products join sales_order so on products."_ProductID" = so."_ProductID"
group by "Product Name"
order by total_units_sold desc
limit 1;

--2.6
select "Product Name",sum("Order Quantity") total_units_sold,p."_ProductID"
from sales_order
join(select *
     from store_locations
     order by "Water Area" desc
     limit 1) as HWA on sales_order."_StoreID" = HWA."_StoreID"
join products p on sales_order."_ProductID" = p."_ProductID"
group by "Product Name", p."_ProductID"
order by total_units_sold desc
limit 1;

--2.7
select  "Region",avg(date_part('day',"DeliveryDate"-"OrderDate")) avg_delivery_in_days
from store_locations
join (select *
      from regions
      where "Region" ='Northeast') as NER on store_locations."StateCode"=NER."StateCode"
join sales_order so on store_locations."_StoreID" = so."_StoreID"
group by NER."Region";

--2.8
select "Sales Team",sum("Order Quantity"* ("Unit Price" - "Unit Cost")) Profit
from sales_team join sales_order so on sales_team."_SalesTeamID" = so."_SalesTeamID"
group by "Sales Team"
order by Profit desc
limit 1;









