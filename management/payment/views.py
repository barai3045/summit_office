from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
import fiscalyear
import math
from io import BytesIO
from num2words import num2words
from xhtml2pdf import pisa
from hr.funs import EmpOffice, EmpTitle
from management.funs import FiscalYearNumber, FiscalYearText, link_callback

from management.models import Approval, Office, PaymentNote, PaymentNoteApproval, PaymentNoteInvoice, PaymentOthers, PaymentOthersItem, Quotation, QuotationItem, VendorAccount

fiscalyear.setup_fiscal_calendar(start_year='same', start_month=7, start_day=1)

def invoice_home(request):
    template_path = "management/payment/invoice/home.html"

    notes = PaymentNote.objects.all().order_by('-id')

    paginator = Paginator(notes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "xs":page_obj,
    }

    return render(request, template_path, context)


def invoice_view(request, pk):
    template_path = "management/payment/invoice/view.html"
    
    note  = get_object_or_404(PaymentNote, pk=pk)
    
    invocies = PaymentNoteInvoice.objects.all().filter(note=note)

    inv_amount= 0
    for inv in invocies:
        if inv.remark:
            inv.remark = inv.remark
        elif inv.paid:
            inv.remark = "Paid"
        else: 
            inv.remark = "Recomemded for Payment"
        if not inv.paid:
            inv_amount = inv_amount + inv.amount

    plant = EmpOffice(note.raise_by.id, note.date)
    office = 'SPL'
    note.ref = f"{office}/{plant.stitle}/Bill/{note.ref()}"
    note.plant = plant
    note.amount = inv_amount
    note.amount_txt = num2words(inv_amount, lang='en_IN')
    note.pamount = inv_amount-float(note.advance+note.security)
    note.pamount_txt = num2words(inv_amount-float(note.advance+note.security),lang='en_IN')

    note.account = VendorAccount.objects.all().filter(vendor=note.vendor)[0]

    try: 
        appr = PaymentNoteApproval.objects.all().filter(note=note)[0]
        approval = get_object_or_404(Approval, pk=appr.approval.id)
        note.approval = approval
        
    except Exception as e: 
        error = e

    context = {
        'x':note,
        'xs2':invocies,
    }
    
    
    
    return render(request, template_path, context)

def invoice_report(request, pk):
    template_path = "management/payment/invoice/report.html"
    note  = get_object_or_404(PaymentNote, pk=pk)
   
    invocies = PaymentNoteInvoice.objects.all().filter(note=note)

    inv_amount= 0
    for inv in invocies:
        if inv.remark:
            inv.remark = inv.remark
        elif inv.paid:
            inv.remark = "Paid"
        else: 
            inv.remark = "Recomemded for Payment"
        if not inv.paid:
            inv_amount = inv_amount + inv.amount
    
    plant = EmpOffice(note.raise_by.id, note.date)
    office = 'SPL'
    note.ref = f"{office}/{plant.stitle}/Bill/{note.ref()}"
    note.plant = plant

    note.raise_by.title = EmpTitle(note.raise_by.id, note.date)
    note.submitted_to.title = EmpTitle(note.submitted_to.id, note.date)
    note.space = ""
    note.amount = inv_amount
    note.amount_txt = num2words(inv_amount, lang='en_IN')
    note.pamount = inv_amount-float(note.advance+note.security)
    note.pamount_txt = num2words(inv_amount-float(note.advance+note.security),lang='en_IN')

    note.account = VendorAccount.objects.all().filter(vendor=note.vendor)[0]

    try: 
        appr = PaymentNoteApproval.objects.all().filter(note=note)[0]
        approval = get_object_or_404(Approval, pk=appr.approval.id)
        note.approval = approval
        
    except Exception as e: 
        error = e
        
    context = {
        'x':note,
        'xs2':invocies,
    }

    # template_path = 'user_printer.html'
    # context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def others_home(request):
    template_path = "management/payment/others/home.html"

    others = PaymentOthers.objects.all().order_by('-id')

    for x in others: 
        fy1 = FiscalYearNumber(x.date)        
        x.fiscalYear = FiscalYearText(x.date)

        i=0
        for y in others.filter(id__lte=x.id):
            fy2 = FiscalYearNumber(y.date)
            if fy1==fy2:
                i = i+1
        x.sl = i

    paginator = Paginator(others, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "xs":page_obj,
    }

    return render(request, template_path, context)


def others_view(request, pk):
    template_path = "management/payment/others/view.html"
    payment = get_object_or_404(PaymentOthers, pk=pk)
    payments = PaymentOthers.objects.all().order_by('id')

    fy1 = FiscalYearNumber(payment.date)        
    payment.fiscalYear = FiscalYearText(payment.date)

    i=0
    for x in payments.filter(id__lte=payment.id):
        fy2 = FiscalYearNumber(x.date)
        if fy1==fy2:
            i = i+1
    payment.sl = i

    items = PaymentOthersItem.objects.all().filter(payment=payment)
    sum_amount=0
    vat_amount=0
    ait_amount=0
    vat = 0
    ait =0 
    for it in items:
        it.amount = it.quantity*it.price
        sum_amount=sum_amount+it.quantity*it.price
        vat_amount=vat_amount+(it.quantity*it.price)*it.vat/100
        ait_amount=ait_amount+(it.quantity*it.price)*it.ait/100
        vat = it.vat
        ait = it.ait

    gross_amount = sum_amount + vat_amount
    payment.items = items
    payment.vat = vat
    payment.ait = ait
    payment.sum_amount = math.trunc(sum_amount)
    payment.vat_amount = math.trunc(vat_amount)
    payment.ait_amount = math.trunc(ait_amount)
    payment.gross_amount = math.trunc(gross_amount)
    gross_amount_txt = num2words(math.trunc(gross_amount), lang='en_IN')

    plant = EmpOffice(payment.raise_by.id, payment.date)
    office = 'SPL'
    payment.ref = f"{office}/{plant.stitle}/Bill/{payment.ref()}"
    payment.plant = plant

    payment.raise_by.title = EmpTitle(payment.raise_by.id, payment.date)
    payment.submitted_to.title = EmpTitle(payment.submitted_to.id, payment.date)

    payment.salutation = f"Submitted for your kind approval for payment of amount BDT {format(gross_amount, '.2f')} (BDT {gross_amount_txt} only) for above stated purpose"

    payment.account = get_object_or_404(VendorAccount, vendor=payment.vendor.id)
    
    context = {
        'x':payment,
        
    }

    return render(request, template_path, context)


def others_report(request, pk):
    template_path = "management/payment/others/report.html"
    payment = get_object_or_404(PaymentOthers, pk=pk)
    payments = PaymentOthers.objects.all().order_by('id')

    fy1 = FiscalYearNumber(payment.date)        
    payment.fiscalYear = FiscalYearText(payment.date)

    i=0
    for x in payments.filter(id__lte=payment.id):
        fy2 = FiscalYearNumber(x.date)
        if fy1==fy2:
            i = i+1
    payment.sl = i

    items = PaymentOthersItem.objects.all().filter(payment=payment)
    sum_amount=0
    vat_amount=0
    ait_amount=0
    vat = 0
    ait =0 
    for it in items:
        it.amount = it.quantity*it.price
        sum_amount=sum_amount+it.quantity*it.price
        vat_amount=vat_amount+(it.quantity*it.price)*it.vat/100
        ait_amount=ait_amount+(it.quantity*it.price)*it.ait/100
        vat = it.vat
        ait = it.ait

    gross_amount = sum_amount + vat_amount
    payment.items = items

    payment.vat = vat
    payment.ait = ait
    payment.sum_amount = math.trunc(sum_amount)
    payment.vat_amount = math.trunc(vat_amount)
    payment.ait_amount = math.trunc(ait_amount)
    payment.gross_amount = math.trunc(gross_amount)
    payment.gross_amount_txt = num2words(math.trunc(gross_amount), lang='en_IN')

    plant = EmpOffice(payment.raise_by.id, payment.date)
    office = 'SPL'
    payment.ref = f"{office}/{plant.stitle}/Bill/{payment.ref()}"
    payment.plant = plant

    payment.raise_by.title = EmpTitle(payment.raise_by.id, payment.date)
    payment.submitted_to.title = EmpTitle(payment.submitted_to.id, payment.date)

    payment.account = get_object_or_404(VendorAccount, vendor=payment.vendor.id)

    context = {
        'x':payment,
        
    }

    # template_path = 'user_printer.html'
    # context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response