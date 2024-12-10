from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator




def index(request):
    contacts = (Contact.objects
                .filter(show=True)
                .all().order_by("-id"))
                #.order_by("-id")[:15])

    # Paginação, com 13 contatos por pagina
    paginator = Paginator(contacts, 13)
    page_number = request.GET.get("page") 
    page_obj = paginator.get_page(page_number)

    context = {
        "contacts": page_obj,
        'titulo': 'Contatos',
        'ano': datetime.now().year,
        "page_obj": page_obj
    }
   
    return render(
        request,
        "contact/index.html",
        context,
    )

# Mostra detalhes do contato
def contact(request, contact_id):
    #single_contact = (Contact.objects.get(pk=contact_id))
    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True
        )

    context = {
        "contact": single_contact,
        'ano': datetime.now().year,
        'titulo': f'{single_contact.first_name} {single_contact.last_name}'
    }
   
    return render(
        request,
        "contact/contact.html",
        context,
    )

# Busca contatos
def search(request):
    search_value = request.GET.get('q', '').strip()

    if search == '':
        return redirect('contact:index')
     
    contacts = (Contact.objects
                .filter(show=True)
                .filter(
                    Q(first_name__icontains=search_value) |
                    Q(last_name__icontains=search_value) |
                    Q(phone__icontains=search_value) |
                    Q(email__icontains=search_value)
                )
                .order_by("first_name"))
    
    # Paginação, com 13 contatos por pagina
    paginator = Paginator(contacts, 13)
    page_number = request.GET.get("page") 
    page_obj = paginator.get_page(page_number)

    # Destacar a palavra de busca em todos os campos de contacts 
    for contact in page_obj: 
        contact.first_name = highlight(contact.first_name, search_value) 
        contact.last_name = highlight(contact.last_name, search_value) 
        contact.phone = highlight(contact.phone, search_value) 
        contact.email = highlight(contact.email, search_value)
    
    #print(contacts.query)

    context = {
        "contacts": page_obj,
        'titulo': f'Buscar por - {search_value}',
        'ano': datetime.now().year,
        "page_obj": page_obj
    }
   
    return render(
        request,
        "contact/index.html",
        context,
    )

from django.utils.html import mark_safe

def highlight(text, search_value):
    highlighted = text.replace(search_value, f'<span class="highlight">{search_value}</span>')
    return mark_safe(highlighted)

