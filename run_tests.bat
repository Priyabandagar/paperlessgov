@echo off
REM PaperLessGov Test Runner Script
REM Quick script to run all tests with different options

echo ====================================
echo PaperLessGov Test Runner
echo ====================================
echo.

REM Check if virtual environment is active
IF "%VIRTUAL_ENV%"=="" (
    echo [WARNING] Virtual environment not detected.
    echo Consider activating your virtual environment first.
    echo.
)

echo Select test run option:
echo 1. Run all tests (normal)
echo 2. Run all tests (verbose)
echo 3. Run specific test class
echo 4. Run with coverage report
echo 5. Run failed tests only
echo 6. Exit
echo.

set /p choice="Enter your choice (1-6): "

IF "%choice%"=="1" (
    echo.
    echo Running all tests...
    python manage.py test filesys
    goto end
)

IF "%choice%"=="2" (
    echo.
    echo Running all tests with verbose output...
    python manage.py test filesys --verbosity=2
    goto end
)

IF "%choice%"=="3" (
    echo.
    echo Available test classes:
    echo - DepartmentModelTests
    echo - DigitalFileModelTests
    echo - FileAttachmentModelTests
    echo - CommentModelTests
    echo - AuditLogModelTests
    echo - AuthenticationViewTests
    echo - DashboardViewTests
    echo - FileCRUDViewTests
    echo - WorkflowStageTransitionTests
    echo - AuditTrailTests
    echo - PermissionTests
    echo - CommentAndAttachmentTests
    echo - FormValidationTests
    echo - IntegrationTests
    echo - SecurityTests
    echo - PerformanceTests
    echo - ErrorHandlingTests
    echo - NotificationTests
    echo - SystemSettingsTests
    echo.
    set /p testclass="Enter test class name: "
    echo.
    echo Running %testclass%...
    python manage.py test filesys.tests.%testclass% --verbosity=2
    goto end
)

IF "%choice%"=="4" (
    echo.
    echo Checking if coverage is installed...
    pip show coverage >nul 2>&1
    IF %ERRORLEVEL% NEQ 0 (
        echo Coverage not found. Installing...
        pip install coverage
    )
    echo.
    echo Running tests with coverage...
    coverage run --source='.' manage.py test filesys
    coverage report
    echo.
    echo Generating HTML coverage report...
    coverage html
    echo HTML report generated in: htmlcov/index.html
    goto end
)

IF "%choice%"=="5" (
    echo.
    echo This option requires maintaining a list of failed tests.
    echo Not yet implemented.
    goto end
)

IF "%choice%"=="6" (
    echo.
    echo Exiting...
    goto end
)

echo.
echo Invalid choice. Please run the script again.

:end
echo.
echo ====================================
echo Test run completed!
echo ====================================
echo.
echo To view detailed documentation, see: TEST_DOCUMENTATION.md
echo.
pause
