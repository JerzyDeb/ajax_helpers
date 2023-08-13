## Get started
Ajax helpers is a basic Django CRUD views that allows you to manage objects in a modal. This project requires bootstrap, jquery and any jquery package with toasts (in my case I used the Toastify package). 


## Usage
1. Load Bootstrap and JQuery to your project
2. Download `static/js/crud_ajax.js` and load it to your project below JQuery implementation
3. Download `core/ajax_helpers.py` file and paste it tou your Django app folder
4. Create or download `templates/_partials/modal.html` - This is a basic Bootstrap modal without `modal-header`, `modal-body` and `modal-footer` divs. Example:
    ```html
    <!-- modal.html -->
    
    <div class="modal fade" id="BasicModal" tabindex="-1" role="dialog" aria-labelledby="modalLabelBasicModal" aria-hidden="true">
      <div class="modal-dialog modal-lg modal-dialog-scrollable " role="document">
        <div class="modal-content"></div>
      </div>
    </div>
    ```
5. Create `list_partial.html` file - This is a list of your objects which refreshing after successfull action. Content of this file must be in `ajax-list` css class div. Example:
    ```html
    <!-- list_partial.html -->
    
    <div class="ajax-list">
      {% for object in object_list %}
        {{ object }}
      {% endfor %}
   </div>
    ```
6. Create your views based on ajax_helpers views:
    ### DetailView
    ```python
    # views.py
   
   from ajax_helpers import AjaxDetailView 
   
    class YourModelDetailView(AjaxDetailView):
        model = YourModel
        template_name = 'your_detail_template.html'
    
        
    # urls.py
    
    path('url-to-your-detail-view/<int:pk>/', YourModelDetailView.as_view(), name='detail_view')
    ```
    ```html
    <!-- your_detail_template.html -->
   
    <div class="modal-header">
      <h5 class="modal-title">{{ object }} - Detail</h5>
      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
    </div>
    <div class="modal-body">
      <h4>{{ object }}</h4>
    </div>
    <div class="modal-footer">
      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
    </div>
    ```
    ### CreateView
    ```python
    # views.py
   
   from ajax_helpers import AjaxCreateView 
   
    class YourModelDetailView(AjaxCreateView):
        model = YourModel
        form_class = YourModelForm
        template_name = 'your_create_template.html'
        partial_template_name = 'your_partial_template.html'
        
    # urls.py
    
    path('url-to-your-create-view/', YourModelCreateView.as_view(), name='create_view')
    ```
    ```html
    <!-- your_create_template.html -->
   
    <form class="ajax-update-form" method="post">
      <div class="modal-header">
        <h5 class="modal-title">Create new Object </h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        {% csrf_token %}
        {{ form.as_p }}
      </div>
      <div class="modal-footer">
        <button type="submit" class="btn btn-success">Create</button>
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </form>
    ```
    ### UpdateView
    ```python
    # views.py
   
   from ajax_helpers import AjaxUpdateView 
   
    class YourModelDetailView(AjaxUpdateView):
        model = YourModel
        form_class = YourModelForm
        template_name = 'your_update_template.html'
        partial_template_name = 'your_partial_template.html'
        
    # urls.py
    
    path('url-to-your-update-view/<int:pk>/', YourModelUpdateView.as_view(), name='update_view')
    ```
    ```html
    <!-- your_update_template.html -->
   
    <form class="ajax-update-form" method="post">
      <div class="modal-header">
        <h5 class="modal-title">{{ object }} - Update</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        {% csrf_token %}
        {{ form.as_p }}
      </div>
      <div class="modal-footer">
        <button type="submit" class="btn btn-success">Update</button>
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </form>
    ```
   ### DeleteView
    ```python
    # views.py
   
   from ajax_helpers import AjaxDeleteView 
   
    class YourModelDetailView(AjaxDeleteView):
        model = TestModel
        template_name = 'your_delete_template.html'
        partial_template_name = '_partials/list_partial.html'
        
    # urls.py
    
    path('url-to-your-delete-view/<int:pk>/', YourModelDeleteView.as_view(), name='delete_view')
    ```
    ```html
    <!-- your_delete_template.html -->
   
    <form class="ajax-update-form" method="post">
      <div class="modal-header">
        <h5 class="modal-title">{{ object }} - Delete</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        {% csrf_token %}
        <p>Are you sure to delete <b>{{ object }}</b>?</p>
      </div>
      <div class="modal-footer">
        <button type="submit" class="btn btn-danger">Delete</button>
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{% trans 'Close' %}</button>
      </div>
    </form>
    ```
7. Add call to action links in your `list_partial.html` file:
    ```html
    <!-- list_partial.html -->
   
    <a class="create-ajax" href="{% url 'create' %}">Create</a>
    <div class="ajax-list">
      {% for object in object_list %}
        {{ object }}
        <a class="detail-ajax" href="{% url 'detail' object.pk %}">Detail</a>
        <a class="update-ajax" href="{% url 'update' object.pk %}">Update</a>
        <a class="delete-ajax" href="{% url 'delete' object.pk %}">Delete</a>
      {% endfor %}
   </div>
    ```
