<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}PaperLessGov - Digital File Management{% endblock %}</title>

    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap Icons -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css">

    <style>
        :root {
            --bg-primary: #f8fafc;
            --bg-secondary: #ffffff;
            --bg-tertiary: #f1f5f9;
            --text-primary: #1e293b;
            --text-secondary: #64748b;
            --accent-blue: #3b82f6;
            --accent-green: #10b981;
            --accent-red: #ef4444;
            --accent-yellow: #f59e0b;
            --accent-purple: #8b5cf6;
            --border-color: #e2e8f0;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-primary);
            color: var(--text-primary);
            margin: 0;
            padding: 0;
        }

        .navbar {
            background: linear-gradient(90deg, #ffffff 0%, #f8fafc 100%);
            border-bottom: 1px solid var(--border-color);
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }

        .navbar-brand {
            font-weight: 700;
            font-size: 1.5rem;
            color: var(--accent-blue) !important;
        }

        .nav-link {
            color: var(--text-secondary) !important;
            transition: all 0.2s;
        }

        .nav-link:hover,
        .nav-link.active {
            color: var(--accent-blue) !important;
        }

        .main-content {
            padding: 2rem;
            min-height: 100vh;
        }

        .card {
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            margin-bottom: 1.5rem;
            border-radius: 12px;
        }

        .card-header {
            background: var(--bg-tertiary);
            border-bottom: 1px solid var(--border-color);
            font-weight: 600;
            color: var(--text-primary);
            border-radius: 12px 12px 0 0 !important;
            padding: 1rem 1.5rem;
        }

        .stat-card {
            padding: 1.5rem;
            border-radius: 12px;
            color: white;
            transition: transform 0.2s;
        }

        .stat-card:hover {
            transform: translateY(-2px);
        }

        .stat-card-blue { background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); }
        .stat-card-green { background: linear-gradient(135deg, #10b981 0%, #059669 100%); }
        .stat-card-red { background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); }
        .stat-card-yellow { background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); }
        .stat-card-purple { background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%); }

        .stat-value {
            font-size: 2.2rem;
            font-weight: 700;
            margin: 0;
            line-height: 1.2;
        }

        .stat-label {
            font-size: 0.9rem;
            opacity: 0.9;
            margin: 0.5rem 0 0 0;
        }

        /* Workflow stages */
        .stage-badge {
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.85rem;
        }

        .stage-draft { background: #64748b; }
        .stage-pending_review { background: var(--accent-blue); }
        .stage-under_review { background: var(--accent-yellow); color: white; }
        .stage-approved { background: var(--accent-green); }
        .stage-rejected { background: var(--accent-red); }
        .stage-archived { background: #8b5cf6; }

        /* Priority badges */
        .priority-low { color: var(--accent-green); }
        .priority-medium { color: var(--accent-blue); }
        .priority-high { color: var(--accent-yellow); }
        .priority-urgent { color: var(--accent-red); font-weight: 700; }

        .table {
            font-size: 0.9rem;
        }

        .table thead th {
            border-top: none;
            background: var(--bg-tertiary);
            font-weight: 600;
            border-bottom: 2px solid var(--border-color);
            color: var(--text-primary);
        }

        .table tbody tr {
            border-bottom: 1px solid var(--border-color);
            transition: background 0.2s;
            color: var(--text-primary);
        }

        .table tbody tr:hover {
            background: var(--bg-tertiary);
        }

        .form-control,
        .form-select {
            background: #ffffff !important;
            border: 1px solid var(--border-color) !important;
            color: var(--text-primary) !important;
        }

        .form-control:focus,
        .form-select:focus {
            background: #ffffff !important;
            border-color: var(--accent-blue) !important;
            color: var(--text-primary) !important;
            box-shadow: 0 0 0 0.2rem rgba(59, 130, 246, 0.25);
        }

        .form-control::placeholder {
            color: rgba(100, 116, 139, 0.6) !important;
        }

        .form-label {
            color: var(--text-primary) !important;
            font-weight: 500;
        }

        .form-select option {
            background: #ffffff;
            color: var(--text-primary);
        }

        /* Links */
        a:not(.nav-link):not(.btn) {
            color: var(--accent-blue);
            text-decoration: none;
        }

        a:not(.nav-link):not(.btn):hover {
            text-decoration: underline;
            opacity: 0.8;
        }

        /* Buttons */
        .btn-primary {
            background-color: var(--accent-blue);
            border-color: var(--accent-blue);
        }

        .btn-primary:hover {
            background-color: #2563eb;
            border-color: #2563eb;
        }

        .btn-outline-light {
            color: var(--text-primary) !important;
            border-color: var(--border-color) !important;
        }

        .btn-outline-light:hover {
            background: var(--bg-tertiary) !important;
            color: var(--text-primary) !important;
        }

        .btn-outline-secondary {
            border-color: var(--border-color) !important;
            color: var(--text-secondary) !important;
        }

        .btn-outline-secondary:hover {
            background: var(--bg-tertiary) !important;
            color: var(--text-primary) !important;
        }

        /* Close buttons for alerts */
        .btn-close {
            filter: none;
        }

        /* Audit log entries */
        .audit-entry {
            padding: 1rem;
            border-left: 4px solid var(--accent-blue);
            background: var(--bg-tertiary);
            margin-bottom: 1rem;
            border-radius: 8px;
        }

        .audit-entry.create { border-left-color: var(--accent-green); }
        .audit-entry.update { border-left-color: var(--accent-blue); }
        .audit-entry.stage_change { border-left-color: var(--accent-yellow); }
        .audit-entry.approve { border-left-color: var(--accent-green); }
        .audit-entry.reject { border-left-color: var(--accent-red); }
        .audit-entry.archive { border-left-color: var(--accent-purple); }

        /* Comments */
        .comment-box {
            background: var(--bg-tertiary);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 1rem;
        }

        .comment-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.5rem;
        }

        .comment-author {
            font-weight: 600;
            color: var(--accent-blue);
        }

        .comment-time {
            color: var(--text-secondary);
            font-size: 0.85rem;
        }

        /* Page header */
        .page-header {
            margin-bottom: 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .page-title {
            font-size: 1.8rem;
            font-weight: 700;
            margin: 0;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .main-content {
                padding: 1rem;
            }
        }
    </style>

    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="{% url 'filesys:dashboard' %}">
                <i class="bi bi-file-earmark-check"></i> PaperLessGov
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'filesys:dashboard' %}">
                            <i class="bi bi-speedometer2"></i> Dashboard
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'filesys:file_list' %}">
                            <i class="bi bi-files"></i> Files
                        </a>
                    </li>
                    {% if user.is_superuser %}
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'filesys:system_audit_logs' %}">
                            <i class="bi bi-shield-check"></i> Audit Logs
                        </a>
                    </li>
                    {% endif %}
                </ul>
                <ul class="navbar-nav">
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="notificationDropdown" role="button" data-bs-toggle="dropdown">
                            <i class="bi bi-bell"></i>
                            {% if unread_notifications and unread_notifications.count > 0 %}
                            <span class="badge bg-danger">{{ unread_notifications.count }}</span>
                            {% endif %}
                        </a>
                        <ul class="dropdown-menu dropdown-menu-dark">
                            <li><h6 class="dropdown-header">Notifications</h6></li>
                            {% if unread_notifications %}
                                {% for notification in unread_notifications %}
                                <li><a class="dropdown-item" href="#">{{ notification.title }}</a></li>
                                {% empty %}
                                <li><span class="dropdown-item text-muted">No new notifications</span></li>
                                {% endfor %}
                            {% else %}
                                <li><span class="dropdown-item text-muted">No new notifications</span></li>
                            {% endif %}
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="userDropdown" role="button" data-bs-toggle="dropdown">
                            <i class="bi bi-person-circle"></i> {{ user.username }}
                        </a>
                        <ul class="dropdown-menu dropdown-menu-dark">
                            <li><a class="dropdown-item" href="{% url 'filesys:profile' %}"><i class="bi bi-person"></i> My Profile</a></li>
                            <li><a class="dropdown-item" href="/admin/"><i class="bi bi-gear"></i> Admin Panel</a></li>
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item" href="{% url 'filesys:logout' %}"><i class="bi bi-box-arrow-right"></i> Logout</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <div class="main-content">
        <!-- Flash Messages -->
        {% if messages %}
        <div class="alert-container mb-3">
            {% for message in messages %}
            <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                {{ message }}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            </div>
            {% endfor %}
        </div>
        {% endif %}

        {% block content %}{% endblock %}
    </div>

    <!-- Bootstrap 5 JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

    <script>
        // Auto-hide alerts after 5 seconds
        setTimeout(function() {
            const alerts = document.querySelectorAll('.alert');
            alerts.forEach(alert => {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            });
        }, 5000);
    </script>

    {% block extra_js %}{% endblock %}
</body>
</html>
