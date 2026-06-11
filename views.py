{% extends 'filesys/base.html' %}

{% block title %}My Profile - {% endblock %}

{% block content %}
<div class="page-header">
    <h1 class="page-title">
        <i class="bi bi-person-circle"></i> My Profile
    </h1>
    <a href="{% url 'filesys:dashboard' %}" class="btn btn-outline-light">
        <i class="bi bi-arrow-left"></i> Dashboard
    </a>
</div>

<div class="row">
    <!-- User Information -->
    <div class="col-md-4">
        <div class="card">
            <div class="card-body text-center">
                <div class="mb-3">
                    <i class="bi bi-person-circle" style="font-size: 5rem; color: var(--accent-blue);"></i>
                </div>
                <h3 style="color: var(--text-primary);">{{ user.get_full_name|default:user.username }}</h3>
                <p class="text-muted">{{ user.email|default:"No email provided" }}</p>
                <p class="mb-0">
                    <span class="badge bg-primary">Username: {{ user.username }}</span>
                </p>
                <p class="mt-2">
                    {% if user.is_superuser %}
                    <span class="badge bg-danger">Administrator</span>
                    {% else %}
                    <span class="badge bg-info">User</span>
                    {% endif %}
                </p>
                <hr>
                <p class="mb-1" style="color: var(--text-secondary);">
                    <strong>Member Since:</strong>
                </p>
                <p style="color: var(--text-primary);">
                    {{ user.date_joined|date:"F d, Y" }}
                </p>
                <p class="mb-1" style="color: var(--text-secondary);">
                    <strong>Last Login:</strong>
                </p>
                <p style="color: var(--text-primary);">
                    {% if user.last_login %}
                    {{ user.last_login|date:"F d, Y H:i" }}
                    {% else %}
                    First time login
                    {% endif %}
                </p>
            </div>
        </div>
    </div>

    <!-- Statistics -->
    <div class="col-md-8">
        <div class="card mb-4">
            <div class="card-header">
                <i class="bi bi-graph-up"></i> My Statistics
            </div>
            <div class="card-body">
                <div class="row">
                    <div class="col-md-4 mb-3">
                        <div class="stat-card stat-card-blue text-center">
                            <p class="stat-value">{{ created_files }}</p>
                            <p class="stat-label">Files Created</p>
                        </div>
                    </div>
                    <div class="col-md-4 mb-3">
                        <div class="stat-card stat-card-yellow text-center">
                            <p class="stat-value">{{ assigned_files }}</p>
                            <p class="stat-label">Assigned to Me</p>
                        </div>
                    </div>
                    <div class="col-md-4 mb-3">
                        <div class="stat-card stat-card-green text-center">
                            <p class="stat-value">{{ completed_files }}</p>
                            <p class="stat-label">Completed</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Recent Activity -->
        <div class="card">
            <div class="card-header">
                <i class="bi bi-clock-history"></i> Recent Activity
            </div>
            <div class="card-body">
                {% if user.audit_logs.all %}
                <div class="table-responsive">
                    <table class="table table-dark">
                        <thead>
                            <tr>
                                <th>Action</th>
                                <th>File</th>
                                <th>Timestamp</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for log in user.audit_logs.all|slice:":10" %}
                            <tr>
                                <td>
                                    <span class="badge bg-secondary">{{ log.get_action_display }}</span>
                                </td>
                                <td>
                                    {% if log.file %}
                                    <a href="{% url 'filesys:file_detail' log.file.tracking_id %}">
                                        {{ log.file.tracking_id }}
                                    </a>
                                    {% else %}
                                    System
                                    {% endif %}
                                </td>
                                <td>
                                    <small class="text-muted">{{ log.timestamp|timesince }} ago</small>
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
                {% else %}
                <div class="text-center text-muted py-4">
                    <i class="bi bi-clock" style="font-size: 3rem; color: rgba(255,255,255,0.2);"></i>
                    <p class="mt-3">No recent activity</p>
                </div>
                {% endif %}
            </div>
        </div>
    </div>
</div>
{% endblock %}
