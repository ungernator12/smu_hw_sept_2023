-- 1) List the employee number, last name, first name, sex, and salary of each employee.
select
	e.emp_no,
	e.last_name,
	e.first_name,
	e.sex,
	s.salary
from
	employees as e
	join salaries as s on e.emp_no = s.emp_no
order by
	s.salary desc
limit 10;

-- 2) List the first name, last name, hire date for employees who were hired in 1986.
select
	first_name,
	last_name,
	hire_date
from
	employees
where
	extract(year from hire_date) = 1986
order by
	hire_date asc, last_name asc;
	
-- 3) List the manager of each department along with their department number, department name, employee number, last name, and first name.
select
	dm.dept_no,
	d.dept_name,
	dm.emp_no,
	e.last_name,
	e.first_name
from
	dept_manager as dm
	join departments as d on dm.dept_no = d.dept_no
	join employees as e on dm.emp_no = e.emp_no
order by
	e.last_name desc;

-- 4) List the department number for each employee along with that employee’s employee number, last name, first name, and department name.
select
	d.dept_no,
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
from
	employees as e
	join dept_emp as de on e.emp_no = de.emp_no
	join departments as d on d.dept_no = de.dept_no
order by
	e.last_name desc;

-- 5) List first name, last name, and sex of each employee whose first name is Hercules and whose last name begins with the letter B.
select
	first_name,
	last_name,
	sex
from
	employees
where
	first_name = 'Hercules'
	and last_name like 'B%'
order by
	last_name;

-- 6) List each employee in the Sales department, including their employee number, last name, and first name.
select
	e.emp_no,
	e.last_name,
	e.first_name,
	de.emp_no,
	de.dept_no,
	d.dept_no,
	d.dept_name
from
	employees as e
	join dept_emp de on e.emp_no = de.emp_no
	join departments d on de.dept_no = d.dept_no
where
	d.dept_name = 'Sales'
order by
	last_name;

-- 7) List each employee in the Sales and Development departments, including their employee number, last name, first name, and department name.
select
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
from
	employees e
	join dept_emp de on e.emp_no = de.emp_no
	join departments d on de.dept_no = d.dept_no
where
	d.dept_name in ('Sales', 'Development')
order by
	e.last_name asc;

-- 8) List the frequency counts, in descending order, of all the employee last names (that is, how many employees share each last name).
select
	e.last_name,
	count(e.emp_no) as name_count
from
	employees e
group by
	e.last_name
order by
	count(e.emp_no) desc;