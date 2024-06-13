from django.shortcuts import render, get_object_or_404
from .models import Employee


def get_all_reportees(manager):
    reportees = Employee.objects.filter(manager=manager)
    reportees_list = []

    for reportee in reportees:
        reportee_dict = {
            'employee': reportee,
            'reportees': get_all_reportees(reportee)
        }
        reportees_list.append(reportee_dict)

    return reportees_list


def home(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'home.html', context)


def manager_employees(request, manager_id):
    manager = get_object_or_404(Employee, id=manager_id)
    reportees = get_all_reportees(manager)
    context = {
        'manager': manager,
        'reportees': reportees,
    }
    return render(request, 'manager_employees.html', context)
