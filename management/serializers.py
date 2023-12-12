from rest_framework import serializers
from management.models import ItemInTitle, PartItem, PaymentNote, PaymentNoteApproval, PaymentNoteInvoice, PaymentOthers, PaymentOthersItem, PurchaseOrder, PurchaseOrderTerm, Quotation, QuotationItem, Title, TitleItem, Vendor, VendorAddress, VendorContact, VendorAccount, Approval


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"


class VendorAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorAddress
        fields = "__all__"


class VendorContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorContact
        fields = "__all__"


class VendorAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorAccount
        fields = "__all__"



## Approval
class PartItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PartItem
        fields = "__all__"


class TitleItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TitleItem
        fields = "__all__"


class ApprovalSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Approval
        fields = "__all__"


class QuotationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Quotation
        fields = "__all__"


class QuotationItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model = QuotationItem
        fields = "__all__"


class TitleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Title
        fields = "__all__"


class ItemInTitleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ItemInTitle
        fields = "__all__"




class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PurchaseOrder
        fields = "__all__"


class PurchaseOrderTermSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PurchaseOrderTerm
        fields = "__all__"


class PaymentNoteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PaymentNote
        fields = "__all__"


class PaymentNoteInvoiceSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PaymentNoteInvoice
        fields = "__all__"


class PaymentNoteApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentNoteApproval
        fields = "__all__"
        

class PaymentOthersSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PaymentOthers
        fields = "__all__"
        

class PaymentOthersItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PaymentOthersItem
        fields = "__all__"


        