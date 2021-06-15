import django_filters
from .models import *
from django.db.models import Q


class DemandeFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='custom_filter_1', label='Other')
    r = django_filters.CharFilter(method='custom_filter_2', label='Supplier')
    d = django_filters.CharFilter(method='custom_filter_3', label='Delay')
    c = django_filters.CharFilter(method='custom_filter_4', label='Cost')
    AppDate = django_filters.CharFilter(method='custom_filter_5', label='Application Date')
    
    class Meta:
        model = Demande
        fields = ['AppDate', 'r', 'd', 'c', 'q', 'Customer', 'PO_Customer', 'Requester']

    def custom_filter_1(self, queryset, name, value):
        return Demande.objects.filter(
            Q(id__icontains=value) | Q(Project_Ref__designation__icontains=value) | Q(Request_Type__icontains=value) | Q(Speciality__icontains=value)
            | Q(Quotation_Number_1__icontains=value) | Q(Quotation_Number_2__icontains=value) | Q(Quotation_Number_3__icontains=value) | Q(Desired_Delivery_Date__icontains=value) 
            | Q(Devise_1__icontains=value) | Q(Devise_2__icontains=value) | Q(Devise_3__icontains=value) | Q(Application_Date__icontains=value)   
        )

    def custom_filter_2(self, queryset, name, value):
        return Demande.objects.filter(
            Q(Supplier_1__nom__icontains=value) | Q(Supplier_2__nom__icontains=value) | Q(Supplier_3__nom__icontains=value)
        )  

    def custom_filter_3(self, queryset, name, value):
        return Demande.objects.filter(
            Q(Delay_1__icontains=value) | Q(Delay_2__icontains=value) | Q(Delay_3__icontains=value) 
        ) 

    def custom_filter_4(self, queryset, name, value):
        return Demande.objects.filter(
            Q(Initial_Cost_Cotation_1__icontains=value) | Q(Initial_Cost_Cotation_2__icontains=value) | Q(Initial_Cost_Cotation_3__icontains=value)
        ) 

    def custom_filter_5(self, queryset, name, value):
        return Demande.objects.filter(
            Q(Application_Date__icontains=value)
        )     

    