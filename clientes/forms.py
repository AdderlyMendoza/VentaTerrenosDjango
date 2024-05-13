from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)

        self.fields['nombres'].label = 'Nombres'
        self.fields['ap_paterno'].label = 'Apellido Paterno'
        self.fields['ap_materno'].label = 'Apellido Materno'
        self.fields['direccion'].label = 'Dirección'
        self.fields['documento'].label = 'Documento'
        self.fields['celular'].label = 'Celular'
       
       
       
        self.fields['nombres'].widget.attrs['placeholder'] = 'Nombres'
        self.fields['ap_paterno'].widget.attrs['placeholder'] = 'Apellido Paterno'
        self.fields['ap_materno'].widget.attrs['placeholder'] = 'Apellido Materno'
        self.fields['direccion'].widget.attrs['placeholder'] = 'Dirección'
        self.fields['documento'].widget.attrs['placeholder'] = 'Documento'
        self.fields['celular'].widget.attrs['placeholder'] = 'Celular'


        self.fields['nombres'].widget.attrs['class'] = 'form-control'
        self.fields['ap_paterno'].widget.attrs['class'] = 'form-control'
        self.fields['ap_materno'].widget.attrs['class'] = 'form-control'
        self.fields['direccion'].widget.attrs['class'] = 'form-control'
        self.fields['documento'].widget.attrs['class'] = 'form-control'
        self.fields['celular'].widget.attrs['class'] = 'form-control'
     


class VentaForm(forms.ModelForm):
    class Meta:
            model = Venta
            fields = ['cliente', 'proyecto', 'subproyecto', 'precio_venta', 'forma_pago', 'cuotas']
   
    
    def __init__(self, *args, **kwargs):
        proyecto_id = kwargs.pop('proyecto_id', None)
        super().__init__(*args, **kwargs)
        if proyecto_id:
            self.fields['subproyecto'].queryset = Sub_Proyecto.objects.filter(proyecto_id=proyecto_id)

        self.fields['cuotas'].required = False  

        if 'forma_pago' in self.data:
            forma_pago = self.data['forma_pago']
        elif self.instance.pk:
            forma_pago = self.instance.forma_pago
        else:
            forma_pago = None
        
        if forma_pago == 'contado':
            self.fields['cuotas'].widget = forms.HiddenInput()  
            self.fields['cuotas'].label = ''  
            self.initial['cuotas'] = 1  
        
        




class CuotaForm(forms.ModelForm):
    class Meta:
        model = Cuota
        fields = '__all__' 
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
            'fecha_pago': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['monto'].widget.attrs['step'] = '0.01'


