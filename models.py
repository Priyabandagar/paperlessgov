{% extends 'filesys/base.html' %}

{% block title %}{% if file %}Edit File{% else %}New File{% endif %} - {% endblock %}

{% block content %}
<div class="page-header">
    <h1 class="page-title">
        <i class="bi bi-{% if file %}pencil{% else %}plus-circle{% endif %}"></i>
        {% if file %}Edit File{% else %}New File{% endif %}
    </h1>
    <a href="{% if file %}{% url 'filesys:file_detail' file.tracking_id %}{% else %}{% url 'filesys:file_list' %}{% endif %}"
       class="btn btn-outline-light">
        <i class="bi bi-arrow-left"></i> Cancel
    </a>
</div>

<div class="row">
    <div class="col-md-8">
        <div class="card">
            <div class="card-header">
                <i class="bi bi-file-earmark-text"></i>
                {% if file %}Edit File Details{% else %}File Information{% endif %}
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}

                    <!-- File Identification -->
                    <h5 class="mb-3" style="color: var(--text-primary);">File Identification</h5>
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label class="form-label">Title *</label>
                            <input type="text" name="title" class="form-control"
                                   value="{% if file %}{{ file.title }}{% endif %}"
                                   required>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label class="form-label">Reference Number</label>
                            <input type="text" name="reference_number" class="form-control"
                                   value="{% if file %}{{ file.reference_number }}{% endif %}">
                        </div>
                    </div>

                    <!-- Classification -->
                    <h5 class="mb-3 mt-4" style="color: var(--text-primary);">Classification</h5>
                    <div class="row">
                        <div class="col-md-4 mb-3">
                            <label class="form-label">Category *</label>
                            <input type="text" name="category" class="form-control"
                                   value="{% if file %}{{ file.category }}{% endif %}"
                                   required>
                        </div>
                        <div class="col-md-4 mb-3">
                            <label class="form-label">Sub Category</label>
                            <input type="text" name="sub_category" class="form-control"
                                   value="{% if file %}{{ file.sub_category }}{% endif %}">
                        </div>
                        <div class="col-md-4 mb-3">
                            <label class="form-label">Priority *</label>
                            <select name="priority" class="form-select" required>
                                {% for value, label in file_priority_choices %}
                                <option value="{{ value }}"
                                        {% if file and file.priority == value %}selected{% elif not file and value == 'medium' %}selected{% endif %}>
                                    {{ label }}
                                </option>
                                {% endfor %}
                            </select>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label class="form-label">Department *</label>
                            <select name="department" class="form-select" required>
                                <option value="">Select Department</option>
                                {% for dept in departments %}
                                <option value="{{ dept.id }}"
                                        {% if file and file.department_id == dept.id %}selected{% endif %}>
                                    {{ dept.code }} - {{ dept.name }}
                                </option>
                                {% endfor %}
                            </select>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label class="form-label">Confidentiality Level</label>
                            <select name="confidentiality_level" class="form-select">
                                {% for value, label in confidentiality_choices %}
                                <option value="{{ value }}"
                                        {% if file and file.confidentiality_level == value %}selected{% elif not file and value == 'internal' %}selected{% endif %}>
                                    {{ label }}
                                </option>
                                {% endfor %}
                            </select>
                        </div>
                    </div>

                    <!-- Content -->
                    <h5 class="mb-3 mt-4" style="color: var(--text-primary);">Content</h5>
                    <div class="mb-3">
                        <label class="form-label">Subject *</label>
                        <input type="text" name="subject" class="form-control"
                               value="{% if file %}{{ file.subject }}{% endif %}"
                               required>
                    </div>

                    <div class="mb-3">
                        <label class="form-label">Description *</label>
                        <textarea name="description" class="form-control"
                                  rows="5" required>{% if file %}{{ file.description }}{% endif %}</textarea>
                    </div>

                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label class="form-label">Keywords</label>
                            <input type="text" name="keywords" class="form-control"
                                   value="{% if file %}{{ file.keywords }}{% endif %}"
                                   placeholder="Comma separated keywords">
                        </div>
                        <div class="col-md-6 mb-3">
                            <label class="form-label">Tags</label>
                            <input type="text" name="tags" class="form-control"
                                   value="{% if file %}{{ file.tags }}{% endif %}"
                                   placeholder="Comma separated tags">
                        </div>
                    </div>

                    <div class="mb-3">
                        <label class="form-label">Due Date</label>
                        <input type="datetime-local" name="due_date" class="form-control"
                               {% if file and file.due_date %}value="{{ file.due_date|date:'Y-m-d\TH:i' }}"{% endif %}>
                    </div>

                    <div class="alert alert-info">
                        <i class="bi bi-info-circle"></i>
                        <strong>Note:</strong> All files will be created in Draft stage. You can submit them for review after creation.
                    </div>

                    <div class="d-flex gap-2">
                        <button type="submit" class="btn btn-primary">
                            <i class="bi bi-check-circle"></i>
                            {% if file %}Update File{% else %}Create File{% endif %}
                        </button>
                        <a href="{% if file %}{% url 'filesys:file_detail' file.tracking_id %}{% else %}{% url 'filesys:file_list' %}{% endif %}"
                           class="btn btn-outline-secondary">
                            Cancel
                        </a>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <!-- Information Panel -->
    <div class="col-md-4">
        <div class="card">
            <div class="card-header">
                <i class="bi bi-info-circle"></i> Guidelines
            </div>
            <div class="card-body">
                <h6 style="color: var(--text-primary);">File Classification</h6>
                <ul style="color: var(--text-primary); font-size: 0.9rem;">
                    <li><strong>Category:</strong> Main classification</li>
                    <li><strong>Sub Category:</strong> Specific type</li>
                    <li><strong>Priority:</strong> Urgency level</li>
                    <li><strong>Confidentiality:</strong> Access level</li>
                </ul>

                <h6 class="mt-3" style="color: var(--text-primary);">Workflow Stages</h6>
                <ol style="color: var(--text-primary); font-size: 0.9rem;">
                    <li>Draft - Initial creation</li>
                    <li>Pending Review - Submitted</li>
                    <li>Under Review - Being reviewed</li>
                    <li>Approved/Rejected - Final state</li>
                </ol>

                <h6 class="mt-3" style="color: var(--text-primary);">Priority Levels</h6>
                <ul style="color: var(--text-primary); font-size: 0.9rem;">
                    <li><span class="priority-low">Low</span> - Routine matters</li>
                    <li><span class="priority-medium">Medium</span> - Standard priority</li>
                    <li><span class="priority-high">High</span> - Important</li>
                    <li><span class="priority-urgent">Urgent</span> - Immediate attention</li>
                </ul>
            </div>
        </div>

        {% if file %}
        <div class="card">
            <div class="card-header">
                <i class="bi bi-clock-history"></i> File History
            </div>
            <div class="card-body">
                <p style="color: var(--text-primary);">
                    <strong>Tracking ID:</strong><br>
                    {{ file.tracking_id }}
                </p>
                <p style="color: var(--text-primary);">
                    <strong>Current Stage:</strong><br>
                    <span class="stage-badge stage-{{ file.current_stage }}">
                        {{ file.get_current_stage_display }}
                    </span>
                </p>
                <p style="color: var(--text-primary);">
                    <strong>Created:</strong><br>
                    {{ file.created_at|date:"F d, Y H:i" }}
                </p>
                <p style="color: var(--text-primary);">
                    <strong>Last Updated:</strong><br>
                    {{ file.updated_at|date:"F d, Y H:i" }}
                </p>
            </div>
        </div>
        {% endif %}
    </div>
</div>
{% endblock %}
