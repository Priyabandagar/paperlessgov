{% extends 'filesys/base.html' %}

{% block title %}{{ file.title }} - {% endblock %}

{% block content %}
<div class="page-header">
    <div>
        <h1 class="page-title mb-2">
            <i class="bi bi-file-earmark-text"></i> {{ file.title }}
        </h1>
        <p class="mb-0" style="color: var(--text-secondary);">
            <strong>Tracking ID:</strong> {{ file.tracking_id }}
        </p>
    </div>
    <div>
        {% if file.current_stage == 'draft' and file.created_by == user %}
        <a href="{% url 'filesys:file_update' file.tracking_id %}" class="btn btn-outline-secondary me-2">
            <i class="bi bi-pencil"></i> Edit
        </a>
        {% elif file.current_stage == 'draft' %}
        <form method="post" action="{% url 'filesys:submit_for_review' file.tracking_id %}" class="d-inline">
            {% csrf_token %}
            <input type="hidden" name="notes" value="Submitted for review">
            <button type="submit" class="btn btn-primary me-2">
                <i class="bi bi-send"></i> Submit for Review
            </button>
        </form>
        {% elif file.current_stage == 'pending_review' and file.current_assignee == user %}
        <form method="post" action="{% url 'filesys:start_review' file.tracking_id %}" class="d-inline">
            {% csrf_token %}
            <input type="hidden" name="notes" value="Review started">
            <button type="submit" class="btn btn-primary me-2">
                <i class="bi bi-play-circle"></i> Start Review
            </button>
        </form>
        {% elif file.current_stage == 'under_review' and file.current_assignee == user %}
        <form method="post" action="{% url 'filesys:approve_file' file.tracking_id %}" class="d-inline me-2">
            {% csrf_token %}
            <input type="hidden" name="notes" value="File approved">
            <button type="submit" class="btn btn-success">
                <i class="bi bi-check-circle"></i> Approve
            </button>
        </form>
        <button type="button" class="btn btn-danger me-2" data-bs-toggle="modal" data-bs-target="#rejectModal">
            <i class="bi bi-x-circle"></i> Reject
        </button>
        {% endif %}
        <a href="{% url 'filesys:file_list' %}" class="btn btn-outline-secondary">
            <i class="bi bi-arrow-left"></i> Back to Files
        </a>
    </div>
</div>

<!-- File Status Cards -->
<div class="row mb-4">
    <div class="col-md-3">
        <div class="card">
            <div class="card-body">
                <p class="mb-1" style="color: var(--text-secondary);">Current Stage</p>
                <h4 class="mb-0">
                    <span class="stage-badge stage-{{ file.current_stage }}">
                        {{ file.get_current_stage_display }}
                    </span>
                </h4>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card">
            <div class="card-body">
                <p class="mb-1" style="color: var(--text-secondary);">Priority</p>
                <h4 class="mb-0">
                    <span class="priority-{{ file.priority }}">
                        {{ file.get_priority_display|title }}
                    </span>
                </h4>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card">
            <div class="card-body">
                <p class="mb-1" style="color: var(--text-secondary);">Department</p>
                <h4 class="mb-0">{{ file.department.code }}</h4>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card">
            <div class="card-body">
                <p class="mb-1" style="color: var(--text-secondary);">Status</p>
                <h4 class="mb-0">
                    {% if file.is_closed %}
                    <span class="badge bg-secondary">Closed</span>
                    {% else %}
                    <span class="badge bg-success">Open</span>
                    {% endif %}
                </h4>
            </div>
        </div>
    </div>
</div>

<div class="row">
    <!-- File Details -->
    <div class="col-md-8">
        <!-- Basic Information -->
        <div class="card mb-4">
            <div class="card-header">
                <i class="bi bi-info-circle"></i> File Information
            </div>
            <div class="card-body">
                <div class="row">
                    <div class="col-md-6 mb-3">
                        <p class="mb-1" style="color: var(--text-secondary);">File Number</p>
                        <p class="mb-0"><strong>{{ file.file_number }}</strong></p>
                    </div>
                    <div class="col-md-6 mb-3">
                        <p class="mb-1" style="color: var(--text-secondary);">Reference Number</p>
                        <p class="mb-0">
                            {% if file.reference_number %}
                            <strong>{{ file.reference_number }}</strong>
                            {% else %}
                            <span class="text-muted">Not provided</span>
                            {% endif %}
                        </p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6 mb-3">
                        <p class="mb-1" style="color: var(--text-secondary);">Category</p>
                        <p class="mb-0"><strong>{{ file.category }}</strong></p>
                    </div>
                    <div class="col-md-6 mb-3">
                        <p class="mb-1" style="color: var(--text-secondary);">Sub Category</p>
                        <p class="mb-0">
                            {% if file.sub_category %}
                            <strong>{{ file.sub_category }}</strong>
                            {% else %}
                            <span class="text-muted">Not specified</span>
                            {% endif %}
                        </p>
                    </div>
                </div>
                <div class="mb-3">
                    <p class="mb-1" style="color: var(--text-secondary);">Subject</p>
                    <p class="mb-0"><strong>{{ file.subject }}</strong></p>
                </div>
                <div class="mb-3">
                    <p class="mb-1" style="color: var(--text-secondary);">Description</p>
                    <p class="mb-0">{{ file.description }}</p>
                </div>
                {% if file.keywords %}
                <div class="mb-3">
                    <p class="mb-1" style="color: var(--text-secondary);">Keywords</p>
                    <p class="mb-0">{{ file.keywords }}</p>
                </div>
                {% endif %}
                {% if file.tags %}
                <div class="mb-0">
                    <p class="mb-1" style="color: var(--text-secondary);">Tags</p>
                    <p class="mb-0">{{ file.tags }}</p>
                </div>
                {% endif %}
            </div>
        </div>

        <!-- Audit Trail -->
        <div class="card mb-4">
            <div class="card-header">
                <i class="bi bi-clock-history"></i> Audit Trail
                <a href="{% url 'filesys:audit_trail' file.tracking_id %}" class="btn btn-sm btn-outline-primary ms-2">
                    View Full Trail
                </a>
            </div>
            <div class="card-body">
                <div class="table-responsive">
                    <table class="table">
                        <thead>
                            <tr>
                                <th>Action</th>
                                <th>User</th>
                                <th>Notes</th>
                                <th>Time</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for log in audit_logs|slice:":5" %}
                            <tr>
                                <td>
                                    <span class="badge bg-secondary">{{ log.get_action_display }}</span>
                                </td>
                                <td>
                                    {% if log.user %}
                                    {{ log.user.get_full_name|default:log.user.username }}
                                    {% else %}
                                    System
                                    {% endif %}
                                </td>
                                <td>{{ log.notes|truncatewords:10 }}</td>
                                <td>
                                    <small class="text-muted">{{ log.timestamp|timesince }} ago</small>
                                </td>
                            </tr>
                            {% empty %}
                            <tr>
                                <td colspan="4" class="text-center text-muted py-3">
                                    No audit trail yet
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- Comments Section -->
        <div class="card">
            <div class="card-header">
                <i class="bi bi-chat-left-text"></i> Comments ({{ comments|length }})
            </div>
            <div class="card-body">
                <!-- Add Comment Form -->
                <form method="post" action="{% url 'filesys:add_comment' file.tracking_id %}" class="mb-4">
                    {% csrf_token %}
                    <div class="mb-3">
                        <textarea name="content" class="form-control" rows="3" placeholder="Add a comment..." required></textarea>
                    </div>
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <select name="comment_type" class="form-select">
                                <option value="note">General Note</option>
                                <option value="review">Review Comment</option>
                                <option value="info">Information</option>
                            </select>
                        </div>
                        <div class="col-md-6 mb-3">
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" name="is_internal" id="is_internal" checked>
                                <label class="form-check-label" for="is_internal">
                                    Internal only
                                </label>
                            </div>
                        </div>
                    </div>
                    <button type="submit" class="btn btn-primary">
                        <i class="bi bi-send"></i> Add Comment
                    </button>
                </form>

                <!-- Comments List -->
                {% for comment in comments %}
                <div class="comment-box">
                    <div class="comment-header">
                        <div>
                            <span class="comment-author">{{ comment.author.get_full_name|default:comment.author.username }}</span>
                            {% if comment.comment_type != 'note' %}
                            <span class="badge bg-info ms-2">{{ comment.get_comment_type_display }}</span>
                            {% endif %}
                            {% if comment.is_internal %}
                            <span class="badge bg-secondary ms-2">Internal</span>
                            {% endif %}
                        </div>
                        <span class="comment-time">{{ comment.created_at|timesince }} ago</span>
                    </div>
                    <p class="mb-0" style="color: var(--text-primary);">{{ comment.content }}</p>
                </div>
                {% empty %}
                <p class="text-center text-muted">No comments yet. Be the first to comment!</p>
                {% endfor %}
            </div>
        </div>
    </div>

    <!-- Sidebar -->
    <div class="col-md-4">
        <!-- Ownership -->
        <div class="card mb-4">
            <div class="card-header">
                <i class="bi bi-people"></i> Ownership
            </div>
            <div class="card-body">
                <div class="mb-3">
                    <p class="mb-1" style="color: var(--text-secondary);">Created By</p>
                    <p class="mb-0"><strong>{{ file.created_by.get_full_name|default:file.created_by.username }}</strong></p>
                    <small class="text-muted">{{ file.created_at|date:"F d, Y H:i" }}</small>
                </div>
                {% if file.current_assignee %}
                <div class="mb-0">
                    <p class="mb-1" style="color: var(--text-secondary);">Assigned To</p>
                    <p class="mb-0"><strong>{{ file.current_assignee.get_full_name|default:file.current_assignee.username }}</strong></p>
                </div>
                {% else %}
                <p class="mb-0"><span class="text-muted">Unassigned</span></p>
                {% endif %}
            </div>
        </div>

        <!-- Timeline -->
        <div class="card mb-4">
            <div class="card-header">
                <i class="bi bi-calendar3"></i> Timeline
            </div>
            <div class="card-body">
                <div class="mb-3">
                    <p class="mb-1" style="color: var(--text-secondary);">Created</p>
                    <p class="mb-0"><small>{{ file.created_at|date:"M d, Y H:i" }}</small></p>
                </div>
                {% if file.submitted_at %}
                <div class="mb-3">
                    <p class="mb-1" style="color: var(--text-secondary);">Submitted</p>
                    <p class="mb-0"><small>{{ file.submitted_at|date:"M d, Y H:i" }}</small></p>
                </div>
                {% endif %}
                {% if file.reviewed_at %}
                <div class="mb-3">
                    <p class="mb-1" style="color: var(--text-secondary);">Reviewed</p>
                    <p class="mb-0"><small>{{ file.reviewed_at|date:"M d, Y H:i" }}</small></p>
                </div>
                {% endif %}
                {% if file.approved_at %}
                <div class="mb-3">
                    <p class="mb-1" style="color: var(--text-secondary);">Approved</p>
                    <p class="mb-0"><small>{{ file.approved_at|date:"M d, Y H:i" }}</small></p>
                </div>
                {% endif %}
                {% if file.due_date %}
                <div class="mb-0">
                    <p class="mb-1" style="color: var(--text-secondary);">Due Date</p>
                    <p class="mb-0">
                        <small class="{% if file.is_overdue %}text-danger{% else %}text-success{% endif %}">
                            {{ file.due_date|date:"M d, Y H:i" }}
                            {% if file.is_overdue %}
                            <i class="bi bi-exclamation-triangle"></i> Overdue
                            {% endif %}
                        </small>
                    </p>
                </div>
                {% endif %}
            </div>
        </div>

        <!-- Attachments -->
        <div class="card">
            <div class="card-header">
                <i class="bi bi-paperclip"></i> Attachments
                <span class="badge bg-secondary ms-2">{{ attachments|length }}</span>
            </div>
            <div class="card-body">
                <!-- Upload Attachment Form -->
                {% if file.created_by == user or file.current_assignee == user or user.is_superuser %}
                <form method="post" action="{% url 'filesys:upload_attachment' file.tracking_id %}" enctype="multipart/form-data" class="mb-3">
                    {% csrf_token %}
                    <div class="mb-2">
                        <input type="file" name="attachment" class="form-control" required>
                    </div>
                    <div class="mb-2">
                        <input type="text" name="description" class="form-control" placeholder="Description (optional)">
                    </div>
                    <button type="submit" class="btn btn-sm btn-primary">
                        <i class="bi bi-upload"></i> Upload
                    </button>
                </form>
                {% endif %}

                <!-- Attachments List -->
                {% for attachment in attachments %}
                <div class="d-flex justify-content-between align-items-center mb-2 p-2" style="background: var(--bg-tertiary); border-radius: 8px;">
                    <div>
                        <strong style="font-size: 0.9rem;">
                            <i class="bi bi-file-earmark"></i> {{ attachment.original_filename|truncatewords:3 }}
                        </strong>
                        <br>
                        <small class="text-muted">
                            {{ attachment.upload_date|date:"M d, Y" }} • {{ attachment.file_size|filesizeformat }}
                        </small>
                    </div>
                    <a href="{% url 'filesys:download_attachment' attachment.id %}" class="btn btn-sm btn-outline-primary">
                        <i class="bi bi-download"></i>
                    </a>
                </div>
                {% empty %}
                <p class="text-center text-muted mb-0">No attachments</p>
                {% endfor %}
            </div>
        </div>
    </div>
</div>

<!-- Reject Modal -->
<div class="modal fade" id="rejectModal" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Reject File</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <form method="post" action="{% url 'filesys:reject_file' file.tracking_id %}">
                {% csrf_token %}
                <div class="modal-body">
                    <div class="mb-3">
                        <label class="form-label">Reason for Rejection *</label>
                        <textarea name="reason" class="form-control" rows="4" required placeholder="Please explain why this file is being rejected..."></textarea>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                    <button type="submit" class="btn btn-danger">
                        <i class="bi bi-x-circle"></i> Reject File
                    </button>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}
