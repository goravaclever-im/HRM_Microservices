from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    Boolean,
    Float,
    ForeignKey,
    UniqueConstraint,
    Index,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False, default="My Organization")
    job_id_prefix = Column(String, default="JOB")

    address = Column(String, nullable=True)
    contact = Column(String, nullable=True)
    email = Column(String, nullable=True)

    logo_storage_path = Column(String, nullable=True)
    logo_storage_url = Column(String, nullable=True)
    logo_storage_provider = Column(String, nullable=True)

    customize_org = Column(Boolean, default=True)

    currency = Column(String, default="USD")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)

    email = Column(String, unique=True, nullable=False)

    password = Column(String, nullable=False)

    role = Column(String, default="EMPLOYEE")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    employee = relationship(
        "Employee",
        back_populates="user",
        uselist=False
    )
class Department(Base):
    __tablename__ = "departments"

    id = Column(String, primary_key=True)

    name = Column(String, unique=True, nullable=False)

    description = Column(String, nullable=True)

    manager_id = Column(String, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    employees = relationship(
        "Employee",
        back_populates="department"
    )

    positions = relationship(
        "Position",
        back_populates="department"
    )

    locations = relationship(
        "Location",
        back_populates="department"
    )
class Location(Base):
    __tablename__ = "locations"

    id = Column(String, primary_key=True)

    name = Column(String, nullable=False)

    department_id = Column(
        String,
        ForeignKey("departments.id"),
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    department = relationship(
        "Department",
        back_populates="locations"
    )

    employees = relationship(
        "Employee",
        back_populates="location"
    )
class Position(Base):
    __tablename__ = "positions"

    id = Column(String, primary_key=True)

    title = Column(String, nullable=False)

    description = Column(String, nullable=True)

    level = Column(String, nullable=True)

    department_id = Column(
        String,
        ForeignKey("departments.id"),
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    department = relationship(
        "Department",
        back_populates="positions"
    )

    employees = relationship(
        "Employee",
        back_populates="position"
    )
class Employee(Base):
    __tablename__ = "employees"

    id = Column(String, primary_key=True)

    employee_id = Column(String, unique=True, nullable=False)

    user_id = Column(
        String,
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    first_name = Column(String, nullable=False)

    last_name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    phone = Column(String, nullable=True)

    date_of_birth = Column(DateTime, nullable=True)

    gender = Column(String, nullable=True)

    address = Column(String, nullable=True)

    city = Column(String, nullable=True)

    country = Column(String, nullable=True)

    avatar = Column(String, nullable=True)

    department_id = Column(
        String,
        ForeignKey("departments.id"),
        nullable=True,
    )

    position_id = Column(
        String,
        ForeignKey("positions.id"),
        nullable=True,
    )

    location_id = Column(
        String,
        ForeignKey("locations.id"),
        nullable=True,
    )

    manager_id = Column(
        String,
        ForeignKey("employees.id", ondelete="SET NULL"),
        nullable=True,
    )

    employment_type = Column(
        String,
        default="FULL_TIME",
    )

    status = Column(
        String,
        default="ACTIVE",
    )

    joining_date = Column(
        DateTime,
        nullable=False,
    )

    leaving_date = Column(
        DateTime,
        nullable=True,
    )

    salary = Column(
        Float,
        nullable=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    # Relationships

    user = relationship(
        "User",
        back_populates="employee",
    )

    department = relationship(
        "Department",
        back_populates="employees",
    )

    position = relationship(
        "Position",
        back_populates="employees",
    )

    location = relationship(
        "Location",
        back_populates="employees",
    )

    manager = relationship(
        "Employee",
        remote_side=[id],
        back_populates="subordinates",
    )

    subordinates = relationship(
        "Employee",
        back_populates="manager",
    )
    subordinates = relationship(
        "Employee",
        back_populates="manager",
    )

    attendances = relationship(
        "Attendance",
        back_populates="employee",
    )

    leave_requests = relationship(
        "LeaveRequest",
        back_populates="employee",
    )

    leave_balances = relationship(
        "LeaveBalance",
        back_populates="employee",
    )

    payslips = relationship(
        "Payslip",
        back_populates="employee",
    )

    performances = relationship(
        "Performance",
        back_populates="employee",
    )
    bank_details = relationship(
        "BankDetails",
        back_populates="employee",
        uselist=False,
    )

    onboarding_record = relationship(
        "OnboardingRecord",
        back_populates="employee",
        uselist=False,
    )

    candidate_documents = relationship(
        "CandidateDocument",
        back_populates="employee",
    )

    compliance_records = relationship(
        "ComplianceRecord",
        back_populates="employee",
    )

    resignations_submitted = relationship(
        "Resignation",
        foreign_keys="Resignation.employee_id",
        back_populates="employee",
    )

    resignations_reviewed = relationship(
        "Resignation",
        foreign_keys="Resignation.reviewed_by_id",
        back_populates="reviewed_by",
    )
    
    timesheets = relationship(
    "Timesheet",
    back_populates="employee",
    )
class Attendance(Base):
    __tablename__ = "attendances"

    id = Column(String, primary_key=True)

    employee_id = Column(
        String,
        ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
    )

    date = Column(DateTime, nullable=False)

    clock_in = Column(DateTime, nullable=True)

    clock_out = Column(DateTime, nullable=True)

    status = Column(String, default="PRESENT")

    work_hours = Column(Float, nullable=True)

    note = Column(String, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    employee = relationship(
        "Employee",
        back_populates="attendances",
    )
class LeaveType(Base):
    __tablename__ = "leave_types"

    id = Column(String, primary_key=True)

    name = Column(String, unique=True, nullable=False)

    code = Column(String, unique=True, nullable=True)

    category = Column(String, default="PAID")

    enterprise_category = Column(String, nullable=True)

    enterprise_sub_category = Column(String, nullable=True)

    annual_allowance = Column(Integer, default=0)

    accrual_rate_per_month = Column(Float, default=0)

    carry_forward_allowed = Column(Boolean, default=False)

    max_carry_forward = Column(Integer, default=0)

    lapses_at_year_end = Column(Boolean, default=False)

    requires_document = Column(Boolean, default=False)

    days_allowed = Column(Integer, default=0)

    description = Column(String, nullable=True)

    leave_requests = relationship(
        "LeaveRequest",
        back_populates="leave_type",
    )

    leave_balances = relationship(
        "LeaveBalance",
        back_populates="leave_type",
    )
class LeaveRequest(Base):
    __tablename__ = "leave_requests"

    id = Column(String, primary_key=True)

    employee_id = Column(
        String,
        ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
    )

    leave_type_id = Column(
        String,
        ForeignKey("leave_types.id"),
        nullable=False,
    )

    start_date = Column(DateTime, nullable=False)

    end_date = Column(DateTime, nullable=False)

    day_portion = Column(String, default="FULL")

    days = Column(Float, nullable=False)

    reason = Column(String, nullable=True)

    attachment_original_name = Column(String, nullable=True)

    attachment_mime_type = Column(String, nullable=True)

    attachment_file_size = Column(Integer, nullable=True)

    attachment_storage_path = Column(String, nullable=True)

    attachment_storage_url = Column(String, nullable=True)

    attachment_storage_provider = Column(String, nullable=True)

    status = Column(String, default="PENDING")

    approved_by_id = Column(String, nullable=True)

    approved_at = Column(DateTime, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    employee = relationship(
        "Employee",
        back_populates="leave_requests",
    )

    leave_type = relationship(
        "LeaveType",
        back_populates="leave_requests",
    )
class LeaveBalance(Base):
    __tablename__ = "leave_balances"

    id = Column(String, primary_key=True)

    employee_id = Column(
        String,
        ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
    )

    leave_type_id = Column(
        String,
        ForeignKey("leave_types.id", ondelete="CASCADE"),
        nullable=False,
    )

    year = Column(Integer, nullable=False)

    opening_days = Column(Float, default=0)

    accrued_days = Column(Float, default=0)

    carry_forward_days = Column(Float, default=0)

    used_days = Column(Float, default=0)

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    employee = relationship(
        "Employee",
        back_populates="leave_balances",
    )

    leave_type = relationship(
        "LeaveType",
        back_populates="leave_balances",
    )

    __table_args__ = (
        UniqueConstraint(
            "employee_id",
            "leave_type_id",
            "year",
            name="uq_leave_balance",
        ),
        Index(
            "idx_leave_balance_employee_year",
            "employee_id",
            "year",
        ),
    )
class Payslip(Base):
    __tablename__ = "payslips"

    id = Column(String, primary_key=True)

    employee_id = Column(
        String,
        ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
    )

    month = Column(Integer, nullable=False)

    year = Column(Integer, nullable=False)

    basic_salary = Column(Float, nullable=False)

    allowances = Column(Float, default=0)

    deductions = Column(Float, default=0)

    tax = Column(Float, default=0)

    net_salary = Column(Float, nullable=False)

    status = Column(String, default="DRAFT")

    paid_at = Column(DateTime, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    employee = relationship(
        "Employee",
        back_populates="payslips",
    )

    __table_args__ = (
        UniqueConstraint(
            "employee_id",
            "month",
            "year",
            name="uq_payslip_employee_month_year",
        ),
    )
class Performance(Base):
    __tablename__ = "performances"

    id = Column(String, primary_key=True)

    employee_id = Column(
        String,
        ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
    )

    reviewer_id = Column(
        String,
        nullable=True,
    )

    period = Column(
        String,
        nullable=False,
    )

    rating = Column(
        Float,
        nullable=True,
    )

    goals = Column(
        String,
        nullable=True,
    )

    achievements = Column(
        String,
        nullable=True,
    )

    feedback = Column(
        String,
        nullable=True,
    )

    manager_feedback = Column(
        String,
        nullable=True,
    )

    status = Column(
        String,
        default="PENDING",
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    employee = relationship(
        "Employee",
        back_populates="performances",
    )
class BankDetails(Base):
    __tablename__ = "bank_details"

    id = Column(String, primary_key=True)

    employee_id = Column(
        String,
        ForeignKey("employees.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    account_holder_name = Column(String, nullable=True)

    bank_name = Column(String, nullable=True)

    account_number = Column(String, nullable=True)

    ifsc_code = Column(String, nullable=True)

    pan_number = Column(String, nullable=True)

    pending_bank_name = Column(String, nullable=True)

    pending_account_number = Column(String, nullable=True)

    pending_ifsc_code = Column(String, nullable=True)

    pending_pan_number = Column(String, nullable=True)

    pending_submitted_at = Column(
        DateTime,
        nullable=True,
    )

    pending_approved_at = Column(
        DateTime,
        nullable=True,
    )

    pending_approved_by_user_id = Column(
        String,
        nullable=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    employee = relationship(
        "Employee",
        back_populates="bank_details",
    )
class OnboardingRecord(Base):
    __tablename__ = "onboarding_records"

    id = Column(String, primary_key=True)

    employee_id = Column(
        String,
        ForeignKey("employees.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    stage = Column(String, default="CANDIDATE")

    offer_status = Column(String, default="PENDING")

    docs_uploaded = Column(Integer, default=0)

    docs_required = Column(Integer, default=7)

    docs_verified = Column(Boolean, default=False)

    bgv_status = Column(String, default="Pending")

    it_email = Column(String, default="Pending")

    it_laptop = Column(String, default="Pending")

    it_slack = Column(String, default="Pending")

    role_title = Column(String, nullable=True)

    department_name = Column(String, nullable=True)

    manager_name = Column(String, nullable=True)

    checklist_json = Column(String, nullable=True)

    timeline_json = Column(String, nullable=True)

    checklist_locked = Column(Boolean, default=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    employee = relationship(
        "Employee",
        back_populates="onboarding_record",
    )
class CandidateDocument(Base):
    __tablename__ = "candidate_documents"

    id = Column(String, primary_key=True)

    employee_id = Column(
        String,
        ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
    )

    document_type = Column(
        String,
        nullable=False,
    )

    original_name = Column(
        String,
        nullable=False,
    )

    file_name = Column(
        String,
        nullable=False,
    )

    file_size = Column(
        Integer,
        nullable=False,
    )

    mime_type = Column(
        String,
        nullable=False,
    )

    storage_path = Column(
        String,
        nullable=False,
    )

    storage_url = Column(
        String,
        nullable=True,
    )

    storage_provider = Column(
        String,
        default="LOCAL",
    )

    status = Column(
        String,
        default="PENDING",
    )

    rejection_reason = Column(
        String,
        nullable=True,
    )

    reviewed_by_id = Column(
        String,
        nullable=True,
    )

    reviewed_at = Column(
        DateTime,
        nullable=True,
    )

    uploaded_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    employee = relationship(
        "Employee",
        back_populates="candidate_documents",
    )

    __table_args__ = (
        UniqueConstraint(
            "employee_id",
            "document_type",
            name="uq_employee_document_type",
        ),
    )
class ComplianceRecord(Base):
    __tablename__ = "compliance_records"

    id = Column(String, primary_key=True)

    employee_id = Column(
        String,
        ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
    )

    compliance_type = Column(
        String,
        nullable=False,
    )

    file_name = Column(
        String,
        nullable=True,
    )

    file_size = Column(
        Integer,
        nullable=True,
    )

    mime_type = Column(
        String,
        nullable=True,
    )

    storage_path = Column(
        String,
        nullable=True,
    )

    storage_url = Column(
        String,
        nullable=True,
    )

    form_data = Column(
        String,
        nullable=True,
    )

    status = Column(
        String,
        default="PENDING",
    )

    rejection_reason = Column(
        String,
        nullable=True,
    )

    reviewed_by_id = Column(
        String,
        nullable=True,
    )

    reviewed_at = Column(
        DateTime,
        nullable=True,
    )

    submitted_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    employee = relationship(
        "Employee",
        back_populates="compliance_records",
    )

    __table_args__ = (
        UniqueConstraint(
            "employee_id",
            "compliance_type",
            name="uq_employee_compliance_type",
        ),
    )
class Resignation(Base):
    __tablename__ = "resignations"

    id = Column(String, primary_key=True)

    employee_id = Column(
        String,
        ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
    )

    reason = Column(
        String,
        nullable=False,
    )

    notice_period_days = Column(
        Integer,
        default=60,
    )

    last_working_date = Column(
        DateTime,
        nullable=False,
    )

    status = Column(
        String,
        default="PENDING",
    )

    review_note = Column(
        String,
        nullable=True,
    )

    reviewed_by_id = Column(
        String,
        ForeignKey("employees.id", ondelete="SET NULL"),
        nullable=True,
    )

    submitted_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    reviewed_at = Column(
        DateTime,
        nullable=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    employee = relationship(
        "Employee",
        foreign_keys=[employee_id],
        back_populates="resignations_submitted",
    )

    reviewed_by = relationship(
        "Employee",
        foreign_keys=[reviewed_by_id],
        back_populates="resignations_reviewed",
    )

class TimesheetProject(Base):
    __tablename__ = "timesheet_projects"

    id = Column(String, primary_key=True)

    name = Column(String, nullable=False)

    code = Column(
        String,
        unique=True,
        nullable=False,
    )

    description = Column(
        String,
        nullable=True,
    )

    client = Column(
        String,
        nullable=True,
    )

    status = Column(
        String,
        default="ACTIVE",
    )

    billable = Column(
        Boolean,
        default=True,
    )

    is_built_in = Column(
        Boolean,
        default=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    entries = relationship(
        "TimesheetEntry",
        back_populates="project",
    )

    __table_args__ = (
        Index(
            "idx_timesheet_project_status",
            "status",
        ),
    )
class Timesheet(Base):
    __tablename__ = "timesheets"

    id = Column(String, primary_key=True)

    employee_id = Column(
        String,
        ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
    )

    week_start = Column(
        String,
        nullable=False,
    )

    week_end = Column(
        String,
        nullable=False,
    )

    total_hours = Column(
        Float,
        default=0,
    )

    status = Column(
        String,
        default="DRAFT",
    )

    submitted_at = Column(
        DateTime,
        nullable=True,
    )

    manager_note = Column(
        String,
        nullable=True,
    )

    hr_note = Column(
        String,
        nullable=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    employee = relationship(
        "Employee",
        back_populates="timesheets",
    )

    entries = relationship(
        "TimesheetEntry",
        back_populates="timesheet",
        cascade="all, delete-orphan",
    )

    approvals = relationship(
        "TimesheetApproval",
        back_populates="timesheet",
        cascade="all, delete-orphan",
    )

    audit_logs = relationship(
        "TimesheetAuditLog",
        back_populates="timesheet",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        UniqueConstraint(
            "employee_id",
            "week_start",
            name="uq_employee_week_start",
        ),
        Index(
            "idx_timesheet_status",
            "status",
        ),
        Index(
            "idx_timesheet_week_start",
            "week_start",
        ),
    )
class TimesheetEntry(Base):
    __tablename__ = "timesheet_entries"

    id = Column(String, primary_key=True)

    timesheet_id = Column(
        String,
        ForeignKey("timesheets.id", ondelete="CASCADE"),
        nullable=False,
    )

    project_id = Column(
        String,
        ForeignKey("timesheet_projects.id"),
        nullable=False,
    )

    date = Column(
        String,
        nullable=False,
    )

    hours = Column(
        Float,
        nullable=False,
    )

    description = Column(
        String,
        nullable=True,
    )

    is_overtime = Column(
        Boolean,
        default=False,
    )

    overtime_reason = Column(
        String,
        nullable=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    timesheet = relationship(
        "Timesheet",
        back_populates="entries",
    )

    project = relationship(
        "TimesheetProject",
        back_populates="entries",
    )

    __table_args__ = (
        Index(
            "idx_timesheet_entry_date",
            "timesheet_id",
            "date",
        ),
    )
class TimesheetApproval(Base):
    __tablename__ = "timesheet_approvals"

    id = Column(String, primary_key=True)

    timesheet_id = Column(
        String,
        ForeignKey("timesheets.id", ondelete="CASCADE"),
        nullable=False,
    )

    approver_id = Column(
        String,
        nullable=False,
    )

    approver_role = Column(
        String,
        nullable=False,
    )

    action = Column(
        String,
        nullable=False,
    )

    comments = Column(
        String,
        nullable=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    timesheet = relationship(
        "Timesheet",
        back_populates="approvals",
    )

    __table_args__ = (
        Index(
            "idx_timesheet_approval_timesheet",
            "timesheet_id",
        ),
    )
class TimesheetAuditLog(Base):
    __tablename__ = "timesheet_audit_logs"

    id = Column(String, primary_key=True)

    timesheet_id = Column(
        String,
        ForeignKey("timesheets.id", ondelete="CASCADE"),
        nullable=False,
    )

    action = Column(
        String,
        nullable=False,
    )

    performed_by = Column(
        String,
        nullable=False,
    )

    performed_by_email = Column(
        String,
        nullable=True,
    )

    details = Column(
        String,
        nullable=True,
    )

    ip_address = Column(
        String,
        nullable=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    timesheet = relationship(
        "Timesheet",
        back_populates="audit_logs",
    )

    __table_args__ = (
        Index(
            "idx_timesheet_audit_timesheet",
            "timesheet_id",
        ),
    )