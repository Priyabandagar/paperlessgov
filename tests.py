{% extends 'filesys/base.html' %}

{% block title %}Files - {% endblock %}

{% block content %}
<div class="page-header">
    <h1 class="page-title">
        <i class="bi bi-files"></i> All Files
    </h1>
    <div>
        <a href="{% url 'filesys:file_create' %}" class="btn btn-primary">
            <i class="bi bi-plus-circle"></i> New File
        </a>
    </div>
</div>

<!-- Filters -->
<div class="card mb-4">
    <div class="card-body">
        <form method="get" class="row g-3">
            <div class="col-md-3">
                <label class="form-label">Search</label>
                <input type="text" name="search" class="form-control"
                       placeholder="Search by title, ID, subject..."
                       value="{{ search_query }}">
            </div>
            <div class="col-md-2">
                <label class="form-label">Stage</label>
                <select name="stage" class="form-select">
                    <option value="">All Stages</option>
                    {% for value, label in file_stage_choices %}
                    <option value="{{ value }}" {% if stage_filter == value %}selected{% endif %}>
                        {{ label }}
                    </option>
                    {% endfor %}
                </select>
            </div>
            <div class="col-md-2">
                <label class="form-label">Priority</label>
                <select name="priority" class="form-select">
                    <option value="">All Priorities</option>
                    {% for value, label in file_priority_choices %}
                    <option value="{{ value }}" {% if priority_filter == value %}selected{% endif %}>
                        {{ label }}
                    </option>
                    {% endfor %}
                </select>
            </div>
            <div class="col-md-2">
                <label class="form-label">Department</label>
                <select name="department" class="form-select">
                    <option value="">All Departments</option>
                    {% for dept in departments %}
                    <option value="{{ dept.id }}" {% if department_filter == dept.id|stringformat:"s" %}selected{% endif %}>
                        {{ dept.name }}
                    </option>
                    {% endfor %}
                </select>
            </div>
            <div class="col-md-2">
                <label class="form-label">Status</label>
                <select name="status" class="form-select">
                    <option value="">All Status</option>
                    <option value="open" {% if status_filter == 'open' %}selected{% endif %}>Open</option>
                    <option value="closed" {% if status_filter == 'closed' %}selected{% endif %}>Closed</option>
                </select>
            </div>
            <div class="col-md-1 d-flex align-items-end">
                <button type="submit" class="btn btn-primary w-100">
                    <i class="bi bi-filter"></i> Filter
                </button>
            </div>
        </form>
    </div>
</div>

<!-- Files Table -->
<div class="card">
    <div class="card-header">
        <i class="bi bi-list-ul"></i> Files ({{ page_obj.paginator.count }} total)
    </div>
    <div class="card-body">
        <div class="table-responsive">
            <table class="table table-dark">
                <thead>
                    <tr>
                        <th>Tracking ID</th>
                        <th>Title</th>
                        <th>Department</th>
                        <th>Category</th>
                        <th>Stage</th>
                        <th>Priority</th>
                        <th>Assignee</th>
                        <th>Created By</th>
                        <th>Created At</th>
                        <th>Due Date</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {% for file in page_obj %}
                    <tr {% if file.is_overdue %}class="table-danger"{% endif %}>
                        <td><strong>{{ file.tracking_id }}</strong></td>
                        <td>{{ file.title|truncatewords:5 }}</td>
                        <td>{{ file.department.code }}</td>
                        <td>{{ file.category }}</td>
                        <td>
                            <span class="stage-badge stage-{{ file.current_stage }}">
                                {{ file.get_current_stage_display }}
                            </span>
                        </td>
                        <td>
                            <span class="priority-{{ file.priority }}">
                                {{ file.get_priority_display|title }}
                            </span>
                        </td>
                        <td>
                            {% if file.current_assignee %}
                            {{ file.current_assignee.username }}
                            {% else %}
                            <span class="text-muted">Unassigned</span>
                            {% endif %}
                        </td>
                        <td>{{ file.created_by.username }}</td>
                        <td>{{ file.created_at|date:"M d, Y" }}</td>
                        <td>
                            {% if file.due_date %}
                            {% if file.is_overdue %}
                            <span class="text-danger">{{ file.due_date|date:"M d" }}</span>
                            {% else %}
                            {{ file.due_date|date:"M d" }}
                            {% endif %}
                            {% else %}
                            <span class="text-muted">-</span>
                            {% endif %}
                        </td>
                        <td>
                            <a href="{% url 'filesys:file_detail' file.tracking_id %}"
                               class="btn btn-sm btn-outline-light">
                                <i class="bi bi-eye"></i> View
                            </a>
                        </td>
                    </tr>
                    {% empty %}
                    <tr>
                        <td colspan="11" class="text-center text-muted py-4">
                            <i class="bi bi-files" style="font-size: 3rem; color: rgba(255,255,255,0.2);"></i>
                            <p class="mt-3">No files found</p>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>

        <!-- Pagination -->
        {% if page_obj.has_other_pages %}
        <nav aria-label="Page navigation" class="mt-3">
            <ul class="pagination justify-content-center">
                {% if page_obj.has_previous %}
                <li class="page-item">
                    <a class="page-link" href="?page=1{% if search_query %}&search={{ search_query }}{% endif %}{% if stage_filter %}&stage={{ stage_filter }}{% endif %}{% if priority_filter %}&priority={{ priority_filter }}{% endif %}{% if department_filter %}&department={{ department_filter }}{% endif %}{% if status_filter %}&status={{ status_filter }}{% endif %}">First</a>
                </li>
                <li class="page-item">
                    <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if search_query %}&search={{ search_query }}{% endif %}{% if stage_filter %}&stage={{ stage_filter }}{% endif %}{% if priority_filter %}&priority={{ priority_filter }}{% endif %}{% if department_filter %}&department={{ department_filter }}{% endif %}{% if status_filter %}&status={{ status_filter }}{% endif %}">Previous</a>
                </li>
                {% endif %}

                <li class="page-item active">
                    <span class="page-link">
                        Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}
                    </span>
                </li>

                {% if page_obj.has_next %}
                <li class="page-item">
                    <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if search_query %}&search={{ search_query }}{% endif %}{% if stage_filter %}&stage={{ stage_filter }}{% endif %}{% if priority_filter %}&priority={{ priority_filter }}{% endif %}{% if department_filter %}&department={{ department_filter }}{% endif %}{% if status_filter %}&status={{ status_filter }}{% endif %}">Next</a>
                </li>
                <li class="page-item">
                    <a class="page-link" href="?page={{ page_obj.paginator.num_pages }}{% if search_query %}&search={{ search_query }}{% endif %}{% if stage_filter %}&stage={{ stage_filter }}{% endif %}{% if priority_filter %}&priority={{ priority_filter }}{% endif %}{% if department_filter %}&department={{ department_filter }}{% endif %}{% if status_filter %}&status={{ status_filter }}{% endif %}">Last</a>
                </li>
                {% endif %}
            </ul>
        </nav>
        {% endif %}
    </div>
</div>
{% endblock %}
