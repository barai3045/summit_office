from django.urls import path
from management import views

app_name = "management"

urlpatterns = [
    path('vendor/', views.VendorList.as_view()),
    path('vendor/<int:pk>', views.VendorDetail.as_view()),
    path('vendor-address/', views.VendorAddressList.as_view()),
    path('vendor-address/<int:pk>', views.VendorAddressDetail.as_view()),
    path('vendor-contact/', views.VendorContactList.as_view()),
    path('vendor-contact/<int:pk>', views.VendorContactDetail.as_view()),
    path('vendor-account/', views.VendorAccountList.as_view()),
    path('vendor-account/<int:pk>', views.VendorAccountDetail.as_view()),
    
    path('part-item/', views.PartItemList.as_view()),
    path('part-item/<str:pk>', views.PartItemDetail.as_view()),
    
    path('title-item/', views.TitleItemList.as_view()),
    path('title-item/<str:pk>', views.TitleItemDetail.as_view()),
    
    path('approval/', views.ApprovalList.as_view()),
    path('approval/<int:pk>', views.ApprovalDetail.as_view()),
    
    path('quotation/', views.QuotationList.as_view()),
    path('quotation/<str:pk>', views.QuotationDetail.as_view()),
    path('quotation-item/', views.QuotationItemList.as_view()),
    path('quotation-item/<int:pk>', views.QuotationItemDetail.as_view()),
    
    path('title/', views.TitleList.as_view()),
    path('title/<int:pk>', views.TitleDetail.as_view()),
    path('itemintitle/', views.ItemInTitleList.as_view()),
    path('itemintitle/<int:pk>', views.ItemInTitleDetail.as_view()),

    path('purchase-order/', views.PurchaseOrderList.as_view()),
    path('purchase-order/<int:pk>', views.PurchaseOrderDetail.as_view()),
    path('purchase-order-term/', views.PurchaseOrderTermList.as_view()),
    path('purchase-order-term/<int:pk>', views.PurchaseOrderTermDetail.as_view()),

    path('payment-note/', views.PaymentNoteList.as_view()),
    path('payment-note/<int:pk>', views.PaymentNoteDetail.as_view()),
    path('payment-note-invoice/', views.PaymentNoteInvoiceList.as_view()),
    path('payment-note-invoice/<int:pk>', views.PaymentNoteInvoiceDetail.as_view()),
    path('payment-note-approval/', views.PaymentNoteApprovalList.as_view()),
    path('payment-note-approval/<int:pk>', views.PaymentNoteApprovalDetail.as_view()),
   
    path('payment-others/', views.PaymentOthersList.as_view()),
    path('payment-others/<int:pk>', views.PaymentOthersDetail.as_view()),
    path('payment-others-item/', views.PaymentOthersItemList.as_view()),
    path('payment-others-item/<int:pk>', views.PaymentOthersItemDetail.as_view()),
]