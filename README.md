## Ajax CRUD views usage:

### Basic modal:
```html
<!-- modal.html -->

<div class="modal fade" id="BasicModal" tabindex="-1" role="dialog" aria-labelledby="modalLabelBasicModal" aria-hidden="true">
  <div class="modal-dialog modal-lg modal-dialog-scrollable " role="document">
    <div class="modal-content"></div>
  </div>
</div>
```

### DetailView:
```python
# views.py

class YourModelDetailView(AjaxDetailView):
    model = YourModel
    template_name = 'your_template.html'

    
# urls.py

path('url-to-your-view/<int:pk>/', YourModelDetailView.as_view, name='detail_view')
```
```html
<!-- your-model-list.html -->
{% for object in object_list %}
  <a href="{% url 'detail_view' object.pk %}" class="detail-ajax">Detail</a>
{% endfor %}
```


