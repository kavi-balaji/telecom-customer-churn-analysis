-- ===================================
-- Telecom Customer Churn Analysis
-- SQL Queries: Data Exploration & Churn Analysis
-- ===================================

-- Create and select database
CREATE DATABASE telecom_project;
use telecom_project;
show tables;

-- Rename table to a clean name
RENAME TABLE `wa_fn-usec_-telco-customer-churn`
TO telecom_customers;

-- View all data
select * from telecom_customers;

-- Check table structure
describe telecom_customers;

-- Total number of customers
select count(*) as total_customers from telecom_customers;

-- Customer count by gender
select gender,count(*) as customer_count 
from telecom_customers group by gender;

-- Customer count by senior citizen status
select SeniorCitizen,count(*) as count
from telecom_customers group by SeniorCitizen;

-- Customer count by contract type
select contract,count(*) as count
from telecom_customers group by contract;

-- Customer count by internet service type
select internetservice,count(*) as count
from telecom_customers group by internetservice;

-- Customer count by payment method
select paymentmethod,count(*) as count
from telecom_customers group by paymentmethod;

-- Average monthly charges across all customers
select round(avg(monthlycharges),2) as avg_customer_pay
from telecom_customers;

-- Highest monthly charge paid
select max(monthlycharges) as highest_customer_pay
from telecom_customers;

-- Average monthly charges by contract type
select contract,round(avg(monthlycharges),2) from telecom_customers 
group by contract;

-- Number of customers by contract type
select contract,count(*) as count_of_customers 
from telecom_customers group by contract;

-- Overall churn count (Yes/No)
select churn,count(*) as count_of_customers from telecom_customers
group by churn;

-- Number of churned customers by contract type
select contract,count(churn) as no_of_churn
from telecom_customers where churn='Yes' group by contract;

-- Number of churned customers by internet service
select internetservice,count(*) as highest_churn
from telecom_customers where churn='Yes' group by internetservice;

-- Number of churned customers by payment method
select paymentmethod,count(*) as highest_churn
from telecom_customers where churn='Yes' group by paymentmethod;

-- Number of churned customers by senior citizen status
select seniorcitizen,count(*) as more_churn
from telecom_customers where churn='Yes' group by seniorcitizen;

-- Total revenue across all customers
select round(sum(totalcharges),3) as total_revenue from telecom_customers;

-- Total revenue by contract type
select contract,sum(totalcharges) as total_revenue from telecom_customers
group by contract;

-- Contract type generating the highest total revenue
select contract,total_revenue from
(select contract,round(sum(totalcharges),2) as total_revenue,
dense_rank() over( order by sum(totalcharges) desc) as ranks
from telecom_customers group by contract)x
where ranks=1;

-- Full data check
select * from telecom_customers;

-- Churn rate by contract type
select contract,count(*) as total_numbers, sum(churn='Yes') as churned_customers,
round(sum(churn='Yes')*100/count(*),2) as churn_rate from telecom_customers group by contract;

-- Churn rate by internet service
select InternetService,count(*) as total_numbers, sum(churn='Yes') as churned_customers,
round(sum(churn='Yes')*100/count(*),2) as churn_rate
from telecom_customers group by InternetService;

-- Churned customers by payment method
select PaymentMethod,count(*) as total_numbers, sum(churn='Yes') as churned_customers
from telecom_customers group by PaymentMethod;

-- Churn rate by senior citizen status
select SeniorCitizen,count(*) as total_numbers, sum(churn='Yes') as churned_customers,
round(sum(churn='Yes')*100/count(*),2) as churn_rate from telecom_customers
group by SeniorCitizen;