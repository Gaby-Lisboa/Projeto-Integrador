from django.http import HttpResponse
import csv
from django.shortcuts import render
from .models import Sensor, TemperaturaData, UmidadeData, LuminosidadeData, ContadorData
from .forms import CSVUploadForm
from dateutil import parser
from django.contrib import messages

def abre_index(request):
    mensagem = "OLÁ TURMA, SEJAM FELIZES SEMPRE!"
    return HttpResponse(mensagem)

def process_csv_upload(request, model_class, expected_fields):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = request.FILES['file']

            if not csv_file.name.endswith('.csv'):
                return render(request, 'upload_csv.html', {'form': form, 'message': 'Este não é um arquivo CSV válido.'})

            file_data = csv_file.read().decode('ISO-8859-1').splitlines()
            reader = csv.DictReader(file_data, delimiter=',')
            success_count = 0  # Contador para o número de registros salvos

            for row in reader:
                try:
                    model_instance = model_class()
                    for field in expected_fields:
                        model_instance.__setattr__(field, row.get(field))
                    model_instance.save()
                    success_count += 1
                except KeyError as e:
                    print(f"Chave {e} não encontrada na linha: {row}")

            return render(request, 'upload_csv.html', {
                'form': form,
                'message': f'Sucesso: {success_count} registro(s) carregado(s) no banco de dados.'
            })
        else:
            return render(request, 'upload_csv.html', {'form': form, 'message': 'Erro no formulário.'})

    else:
        form = CSVUploadForm()

    return render(request, 'upload_csv.html', {'form': form})

def upload_temperatura_view(request):
    expected_fields = ['sensor_id', 'valor', 'timestamp']
    return process_csv_upload(request, TemperaturaData, expected_fields)

def upload_umidade_view(request):
    expected_fields = ['sensor_id', 'valor', 'timestamp']
    return process_csv_upload(request, UmidadeData, expected_fields)

def upload_luminosidade_view(request):
    expected_fields = ['sensor_id', 'valor', 'timestamp']
    return process_csv_upload(request, LuminosidadeData, expected_fields)

def upload_contador_view(request):
    expected_fields = ['sensor_id', 'timestamp']
    return process_csv_upload(request, ContadorData, expected_fields)

def upload_sensores_view(request):
    expected_fields = ['tipo', 'unidade_medida', 'latitude', 'longitude', 'localizacao', 'responsavel', 'status_operacional', 'observacao', 'mac_address']
    return process_csv_upload(request, Sensor, expected_fields)
