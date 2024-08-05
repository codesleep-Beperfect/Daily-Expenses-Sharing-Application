from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Expense, UserModel, ExpenseShare

def generate_balance_sheet_all_users():
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="all_users_balance_sheet.pdf"'

    c = canvas.Canvas(response, pagesize=letter)
    c.drawString(100, 750, "Balance Sheet for All Users")

    y = 720
    users = UserModel.objects.all()
    serial_number = 1
    for user in users:
        c.drawString(100, y, f"{serial_number}.  User:- {user.name}")
        y -= 20
        expenses = Expense.objects.filter(user=user)
        if not expenses:
            c.drawString(120, y, "No expenses recorded.")
            y -= 20

        for expense in expenses:
            c.drawString(120, y, f"{expense.date} - {expense.title}: ${expense.amount}")
            y -= 20
            shares = ExpenseShare.objects.filter(expense=expense)
            alphabet_label = 'a'
            for share in shares:
                c.drawString(140, y, f"{alphabet_label}.  Shared with {share.user.name}: ${share.amount} ({share.share_type})")
                y -= 20
                alphabet_label = chr(ord(alphabet_label) + 1)
            y -= 10  # Extra space between different expenses
        
        y -= 30  # Extra space between different users

        if y < 100:
            c.showPage()
            y = 750
        
        serial_number += 1

    c.showPage()
    c.save()
    return response