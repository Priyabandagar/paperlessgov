{% extends 'filesys/base.html' %}

{% block title %}Dashboard - {% endblock %}

{% block content %}
<div class="page-header">
    <h1 class="page-title">
        <i class="bi bi-speedometer2"></i> Dashboard
    </h1>
    <a href="{% url 'filesys:file_create' %}" class="btn btn-primary">
        <i class="bi bi-plus-circle"></i> New File
    </a>
</div>

<!-- Statistics Cards -->
<div class="row mb-4">
    <div class="col-md-2">
        <div class="stat-card stat-card-blue">
            <p class="stat-value">{{ total_files }}</p>
            <p class="stat-label">Total Files</p>
        </div>
    </div>
    <div class="col-md-2">
        <div class="stat-card" style="background: #64748b;">
            <p class="stat-value">{{ draft_files }}</p>
            <p class="stat-label">Draft</p>
        </div>
    </div>
    <div class="col-md-2">
        <div class="stat-card stat-card-yellow">
            <p class="stat-value">{{ pending_review }}</p>
            <p class="stat-label">Pending Review</p>
        </div>
    </div>
    <div class="col-md-2">
        <div class="stat-card stat-card-purple">
            <p class="stat-value">{{ under_review }}</p>
            <p class="stat-label">Under Review</p>
        </div>
    </div>
    <div class="col-md-2">
        <div class="stat-card stat-card-green">
            <p class="stat-value">{{ approved_files }}</p>
            <p class="stat-label">Approved</p>
        </div>
    </div>
    <div class="col-md-2">
        <div class="stat-card stat-card-red">
            <p class="stat-value">{{ rejected_files }}</p>
            <p class="stat-label">Rejected</p>
        </div>
    </div>
</div>

<div class="row">
    <!-- Pending Actions -->
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <i class="bi bi-clock-history"></i> Pending Actions
                {% if my_pending.count > 0 %}
                <span class="badge bg-warning ms-2">{{ my_pending.count }}</span>
                {% endif %}
            </div>
            <div class="card-body">
                {% if my_pending %}
                <div class="table-responsive">
                    <table class="table table-dark">
                        <thead>
                            <tr>
                                <th>Tracking ID</th>
                                <th>Title</th>
                                <th>Stage</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for file in my_pending %}
                            <tr>
                                <td><strong>{{ file.tracking_id }}</strong></td>
                                <td>{{ file.title|truncatewords:5 }}</td>
                                <td>
                                    <span class="stage-badge stage-{{ file.current_stage }}">
                                        {{ file.get_current_stage_display }}
                                    </span>
                                </td>
                                <td>
                                    <a href="{% url 'filesys:file_detail' file.tracking_id %}"
                                       class="btn btn-sm btn-primary">
                                        <i class="bi bi-eye"></i> View
                                    </a>
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
                {% else %}
                <div class="text-center text-muted py-4">
                    <i class="bi bi-check-circle" style="font-size: 3rem; color: rgba(255,255,255,0.2);"></i>
                    <p class="mt-3">No pending actions</p>
                </div>
                {% endif %}
            </div>
        </div>
    </div>

    <!-- Notifications -->
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <i class="bi bi-bell"></i> Recent Notifications
            </div>
            <div class="card-body">
                {% if unread_notifications %}
                <div class="list-group">
                    {% for notification in unread_notifications %}
                    <a href="#" class="list-group-item list-group-item-action bg-dark text-light border-secondary">
                        <div class="d-flex w-100 justify-content-between">
                            <h6 class="mb-1">{{ notification.title }}</h6>
                            <small>{{ notification.created_at|timesince }} ago</small>
                        </div>
                        <p class="mb-1 small">{{ notification.message }}</p>
                    </a>
                    {% endfor %}
                </div>
                {% else %}
                <div class="text-center text-muted py-4">
                    <i class="bi bi-bell-slash" style="font-size: 3rem; color: rgba(255,255,255,0.2);"></i>
                    <p class="mt-3">No new notifications</p>
                </div>
                {% endif %}
            </div>
        </div>

        <!-- Overdue Files Alert -->
        {% if overdue_files > 0 %}
        <div class="card mt-3 border-danger">
            <div class="card-header bg-danger text-white">
                <i class="bi bi-exclamation-triangle"></i> Overdue Files
            </div>
            <div class="card-body">
                <p class="mb-2">
                    <strong>{{ overdue_files }}</strong> file(s) are overdue and require attention.
                </p>
                <a href="{% url 'filesys:file_list' %}?status=open" class="btn btn-sm btn-danger">
                    View Overdue Files
                </a>
            </div>
        </div>
        {% endif %}
    </div>
</div>

<!-- Recent Files -->
<div class="row mt-4">
    <div class="col-12">
        <div class="card">
            <div class="card-header">
                <i class="bi bi-clock"></i> Recent Files
            </div>
            <div class="card-body">
                <div class="table-responsive">
                    <table class="table table">
                        <thead>
                            <tr>
                                <th>Tracking ID</th>
                                <th>Title</th>
                                <th>Department</th>
                                <th>Stage</th>
                                <th>Priority</th>
                                <th>Created By</th>
                                <th>Created At</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for file in recent_files %}
                            <tr>
                                <td><strong>{{ file.tracking_id }}</strong></td>
                                <td>{{ file.title|truncatewords:5 }}</td>
                                <td>{{ file.department.code }}</td>
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
                                <td>{{ file.created_by.username }}</td>
                                <td>{{ file.created_at|date:"M d, Y" }}</td>
                                <td>
                                    <a href="{% url 'filesys:file_detail' file.tracking_id %}"
                                       class="btn btn-sm btn-outline-light">
                                        <i class="bi bi-eye"></i> View
                                    </a>
                                </td>
                            </tr>
                            {% empty %}
                            <tr>
                                <td colspan="8" class="text-center text-muted py-4">
                                    <i class="bi bi-files" style="font-size: 3rem; color: rgba(255,255,255,0.2);"></i>
                                    <p class="mt-3">No files yet. Create your first file!</p>
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
