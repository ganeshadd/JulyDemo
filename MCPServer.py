
from mcp.server import MCPServer

mcp = MCPServer("Business Assistant")

# Sample business data
employees = [
    {"name": "Amit", "department": "Sales", "salary": 50000},
    {"name": "Priya", "department": "HR", "salary": 60000},
    {"name": "Rahul", "department": "Sales", "salary": 55000},
    {"name": "Sneha", "department": "Finance", "salary": 65000},
    {"name": "Karan", "department": "Sales", "salary": 52000}
]

# TOOL 1: Employee count
@mcp.tool()
def get_employee_count(department: str) -> dict:
    """Get the number of employees in a department."""
    result = [
        e for e in employees
        if e["department"].lower() == department.lower()
    ]

    return {
        "department": department,
        "employee_count": len(result)
    }


# TOOL 2: Discount calculator
@mcp.tool()
def calculate_discount(
    amount: float,
    discount_percentage: float
) -> dict:
    """Calculate discount and final invoice amount."""
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if not 0 <= discount_percentage <= 100:
        raise ValueError("Discount must be between 0 and 100")

    discount = amount * discount_percentage / 100

    return {
        "original_amount": amount,
        "discount": discount,
        "final_amount": amount - discount
    }


# TOOL 3: Sales report
@mcp.tool()
def get_sales_summary() -> dict:
    """Get the company's sample monthly sales summary."""
    sales = {
        "January": 120000,
        "February": 150000,
        "March": 180000
    }

    return {
        "monthly_sales": sales,
        "total_sales": sum(sales.values())
    }


# RESOURCE: Company policy
@mcp.resource("company://leave-policy")
def leave_policy() -> str:
    """Read the company's leave policy."""
    return """
    COMPANY LEAVE POLICY

    Annual leave: 20 days
    Sick leave: 10 days
    Casual leave: 7 days
    Approval: Manager approval required.
    """


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
