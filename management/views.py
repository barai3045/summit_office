from management.models import ItemInTitle, PartItem, PaymentNote, PaymentNoteApproval, PaymentNoteInvoice, PaymentOthers, PaymentOthersItem, PurchaseOrder, PurchaseOrderTerm, Quotation, QuotationItem, Title, TitleItem, Vendor, VendorAddress, VendorContact, VendorAccount, Approval
from management.serializers import ApprovalSerializer, ItemInTitleSerializer, PartItemSerializer, PaymentNoteApprovalSerializer, PaymentNoteInvoiceSerializer, PaymentNoteSerializer, PaymentOthersItemSerializer, PaymentOthersSerializer, PurchaseOrderSerializer, PurchaseOrderTermSerializer, QuotationItemSerializer, QuotationSerializer, TitleItemSerializer, TitleSerializer, VendorSerializer, VendorAddressSerializer, VendorContactSerializer, VendorAccountSerializer
from rest_framework import generics


# Create your views here.
class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorAddressList(generics.ListCreateAPIView):
    queryset = VendorAddress.objects.all()
    serializer_class = VendorAddressSerializer


class VendorAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VendorAddress.objects.all()
    serializer_class = VendorAddressSerializer


class VendorContactList(generics.ListCreateAPIView):
    queryset = VendorContact.objects.all()
    serializer_class = VendorContactSerializer


class VendorContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VendorContact.objects.all()
    serializer_class = VendorContactSerializer


class VendorAccountList(generics.ListCreateAPIView):
    queryset = VendorAccount.objects.all()
    serializer_class = VendorAccountSerializer


class VendorAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VendorAccount.objects.all()
    serializer_class = VendorAccountSerializer


class PartItemList(generics.ListCreateAPIView):
    queryset = PartItem.objects.all()
    serializer_class = PartItemSerializer


class PartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PartItem.objects.all()
    serializer_class = PartItemSerializer


class TitleItemList(generics.ListCreateAPIView):
    queryset = TitleItem.objects.all()
    serializer_class = TitleItemSerializer


class TitleItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TitleItem.objects.all()
    serializer_class = TitleItemSerializer


class ApprovalList(generics.ListCreateAPIView):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer


class ApprovalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer


class QuotationList(generics.ListCreateAPIView):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer


class QuotationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer


class QuotationItemList(generics.ListCreateAPIView):
    queryset = QuotationItem.objects.all()
    serializer_class = QuotationItemSerializer


class QuotationItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuotationItem.objects.all()
    serializer_class = QuotationItemSerializer


class TitleList(generics.ListCreateAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class TitleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class ItemInTitleList(generics.ListCreateAPIView):
    queryset = ItemInTitle.objects.all()
    serializer_class = ItemInTitleSerializer


class ItemInTitleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemInTitle.objects.all()
    serializer_class = ItemInTitleSerializer


class PurchaseOrderList(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PurchaseOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PurchaseOrderTermList(generics.ListCreateAPIView):
    queryset = PurchaseOrderTerm.objects.all()
    serializer_class = PurchaseOrderTermSerializer


class PurchaseOrderTermDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrderTerm.objects.all()
    serializer_class = PurchaseOrderTermSerializer



class PaymentNoteList(generics.ListCreateAPIView):
    queryset = PaymentNote.objects.all()
    serializer_class = PaymentNoteSerializer


class PaymentNoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentNote.objects.all()
    serializer_class = PaymentNoteSerializer


class PaymentNoteInvoiceList(generics.ListCreateAPIView):
    queryset = PaymentNoteInvoice.objects.all()
    serializer_class = PaymentNoteInvoiceSerializer


class PaymentNoteInvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentNoteInvoice.objects.all()
    serializer_class = PaymentNoteInvoiceSerializer


class PaymentNoteApprovalList(generics.ListCreateAPIView):
    queryset = PaymentNoteApproval.objects.all()
    serializer_class = PaymentNoteApprovalSerializer


class PaymentNoteApprovalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentNoteApproval.objects.all()
    serializer_class = PaymentNoteApprovalSerializer


class PaymentOthersList(generics.ListCreateAPIView):
    queryset = PaymentOthers.objects.all()
    serializer_class = PaymentOthersSerializer


class PaymentOthersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentOthers.objects.all()
    serializer_class = PaymentOthersSerializer


class PaymentOthersItemList(generics.ListCreateAPIView):
    queryset = PaymentOthersItem.objects.all()
    serializer_class = PaymentOthersItemSerializer


class PaymentOthersItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentOthersItem.objects.all()
    serializer_class = PaymentOthersItemSerializer
