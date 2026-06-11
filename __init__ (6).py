{% extends 'filesys/base.html' %}

{% block title %}Audit Trail - {{ file.tracking_id }} - {% endblock %}

{% block content %}
<div class="page-header">
    <h1 class="page-title">
        <i class="bi bi-shield-check"></i> Audit Trail
    </h1>
    <div>
        <a href="{% url 'filesys:file_detail' file.tracking_id %}" class="btn btn-outline-secondary">
            <i class="bi bi-arrow-left"></i> Back to File
        </a>
        <a href="{% url 'filesys:file_list' %}" class="btn btn-outline-primary ms-2">
            <i class="bi bi-files"></i> All Files
        </a>
    </div>
</div>

<!-- File Summary -->
<div class="card mb-4">
    <div class="card-body">
        <div class="row">
            <div class="col-md-8">
                <h5 class="mb-1">{{ file.title }}</h5>
                <p class="mb-0" style="color: var(--text-secondary);">
                    <strong>Tracking ID:</strong> {{ file.tracking_id }} |
                    <strong>Stage:</strong>
                    <span class="stage-badge stage-{{ file.current_stage }} ms-1">
                        {{ file.get_current_stage_display }}
                    </span>
                </p>
            </div>
            <div class="col-md-4 text-end">
                <p class="mb-1" style="color: var(--text-secondary);">Total Actions</p>
                <h3 class="mb-0">{{ audit_logs|length }}</h3>
            </div>
        </div>
    </div>
</div>

<!-- Filters -->
<div class="card mb-4">
    <div class="card-body">
        <form method="get" class="row g-3">
            <div class="col-md-4">
                <label class="form-label">Filter by Action</label>
                <select name="action" class="form-select">
                    <option value="">All Actions</option>
                    <option value="create" {% if action_filter == 'create' %}selected{% endif %}>Create</option>
                    <option value="update" {% if action_filter == 'update' %}selected{% endif %}>Update</option>
                    <option value="stage_change" {% if action_filter == 'stage_change' %}selected{% endif %}>Stage Change</option>
                    <option value="approve" {% if action_filter == 'approve' %}selected{% endif %}>Approve</option>
                    <option value="reject" {% if action_filter == 'reject' %}selected{% endif %}>Reject</option>
                    <option value="archive" {% if action_filter == 'archive' %}selected{% endif %}>Archive</option>
                    <option value="add_comment" {% if action_filter == 'add_comment' %}selected{% endif %}>Comment Added</option>
                    <option value="upload_attachment" {% if action_filter == 'upload_attachment' %}selected{% endif %}>Attachment Uploaded</option>
                </select>
            </div>
            <div class="col-md-4">
                <label class="form-label">Filter by User</label>
                <select name="user" class="form-select">
                    <option value="">All Users</option>
                    {% for log in audit_logs %}
                        {% if log.user and log.user.username not in request.GET.user %}
                        <option value="{{ log.user.id }}" {% if user_filter == log.user.id|stringformat:"s" %}selected{% endif %}>
                            {{ log.user.get_full_name|default:log.user.username }}
                        </option>
                        {% endif %}
                    {% endfor %}
                </select>
            </div>
            <div class="col-md-4 d-flex align-items-end">
                <button type="submit" class="btn btn-primary">
                    <i class="bi bi-filter"></i> Apply Filters
                </button>
                {% if action_filter or user_filter %}
                <a href="{% url 'filesys:audit_trail' file.tracking_id %}" class="btn btn-outline-secondary ms-2">
                    Clear
                </a>
                {% endif %}
            </div>
        </form>
    </div>
</div>

<!-- Audit Trail Timeline -->
<div class="card">
    <div class="card-header">
        <i class="bi bi-list-ul"></i> Complete Audit History
    </div>
    <div class="card-body">
        {% if audit_logs %}
        <div class="timeline">
            {% for log in audit_logs %}
            <div class="audit-entry {{ log.action }} mb-3">
                <div class="d-flex justify-content-between align-items-start mb-2">
                    <div>
                        <h6 class="mb-1">
                            <span class="badge bg-primary">{{ log.get_action_display }}</span>
                            {% if log.from_stage and log.to_stage %}
                            <span class="ms-2">
                                <span class="badge bg-secondary">{{ log.get_from_stage_display }}</span>
                                <i class="bi bi-arrow-right mx-1"></i>
                                <span class="badge bg-info">{{ log.get_to_stage_display }}</span>
                            </span>
                            {% endif %}
                        </h6>
                        <p class="mb-1" style="color: var(--text-primary);">
                            {% if log.user %}
                            <strong>{{ log.user.get_full_name|default:log.user.username }}</strong>
                            {% else %}
                            <strong>System</strong>
                            {% endif %}
                            {% if log.related_object_type %}
                            <span class="badge bg-secondary ms-2">{{ log.related_object_type|title }}</span>
                            {% endif %}
                        </p>
                    </div>
                    <small class="text-muted">
                        <i class="bi bi-clock"></i> {{ log.timestamp|date:"M d, Y H:i:s" }}
                        {% if log.ip_address %}
                        | <i class="bi bi-geo"></i> {{ log.ip_address }}
                        {% endif %}
                    </small>
                </div>

                {% if log.notes %}
                <p class="mb-2" style="color: var(--text-primary);">{{ log.notes }}</p>
                {% endif %}

                {% if log.changes_json %}
                <details class="mt-2">
                    <summary style="cursor: pointer; color: var(--accent-blue);">
                        <i class="bi bi-code-square"></i> View Changes
                    </summary>
                    <pre class="mt-2 p-2" style="background: var(--bg-tertiary); border-radius: 5px; font-size: 0.85rem;"><code>{{ log.changes_json|pprint }}</code></pre>
                </details>
                {% endif %}

                {% if log.session_key or log.request_id %}
                <div class="mt-2">
                    <small class="text-muted">
                        {% if log.request_id %}
                        <i class="bi bi-hash"></i> Request: {{ log.request_id }}
                        {% endif %}
                        {% if log.user_agent %}
                        | <i class="bi bi-browser-chrome"></i> {{ log.user_agent|truncatewords:5 }}
                        {% endif %}
                    </small>
                </div>
                {% endif %}
            </div>
            {% endfor %}
        </div>
        {% else %}
        <div class="text-center py-5">
            <i class="bi bi-shield-check" style="font-size: 4rem; color: var(--border-color);"></i>
            <p class="mt-3 text-muted">No audit logs found</p>
        </div>
        {% endif %}
    </div>
</div>

<style>
.timeline {
    position: relative;
    padding-left: 20px;
}

.timeline::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 2px;
    background: var(--border-color);
}

.audit-entry {
    position: relative;
    margin-left: 20px;
}

.audit-entry::before {
    content: '';
    position: absolute;
    left: -26px;
    top: 5px;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: var(--accent-blue);
    border: 2px solid #ffffff;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
}

.audit-entry.create::before {
    background: var(--accent-green);
    box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.2);
}

.audit-entry.approve::before {
    background: var(--accent-green);
    box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.2);
}

.audit-entry.reject::before {
    background: var(--accent-red);
    box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.2);
}

.audit-entry.stage_change::before {
    background: var(--accent-yellow);
    box-shadow: 0 0 0 3px rgba(245, 158, 11, 0.2);
}

.audit-entry.archive::before {
    background: var(--accent-purple);
    box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.2);
}

.audit-entry.update::before {
    background: var(--accent-blue);
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
}

.audit-entry.add_comment::before {
    background: #8b5cf6;
    box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.2);
}

.audit-entry.upload_attachment::before {
    background: #06b6d4;
    box-shadow: 0 0 0 3px rgba(6, 182, 212, 0.2);
}
</style>
{% endblock %}
