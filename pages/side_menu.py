from pages.dashboard_page import DashboardPage

class NavBar(DashboardPage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        
        #--------------Employee Service Main-Menu Bar-------------------------------------
        self.employee_service = page.getByText("Employee Service")

        #--------------- Dashboard sub-menu---------------------------------------------
        self.dashboard_menu = page.get_by_text("Dashboard")

        #-----------------Profile sub-menu----------------------------------------------
        self.profile_menu = page.get_by_text("Profile")

        #-----------------Activity sub-menu-------------------------------------------
        self.activity_menu = page.get_by_text("Activity")

        #--------------------Attendance sub-menu---------------------------------------
        self.attendance_menu = page.get_by_text("Attendance")

        #-------------------------Attendance Correction sub-menu----------------------------
        self.attendance_correction_menu = page.get_by_text("Attendance Correction").first()

        #------------------------Leaves sub-menu-----------------------------------
        self.leaves_menu = page.get_by_text("Leaves")

        #---------------------Comp Off Balance sub-menu--------------------------------------
        self.comp_off_menu = page.get_by_text("Comp Off Balance").first()

        #-------------------------- GatePass sub-menu----------------------------------------
        self.getepass_menu = page.get_by_text("GatePass")

        #-------------------------------- Shift sub-menu--------------------------------
        self.shift_menu = page.get_by_text("Shift")

        #---------------------------------Salary Slip sub-menu------------------------------------
        self.salary_menu = page.get_by_text("Salary Slip")

        #--------------------- Salary Structure sub-menu---------------------------------
        self.salary_structure_menu = page.get_by_text("Salary Structure").first()
       

        #==============================HR Module=========================================
        
        #-----------------HR module Menu ---------------------------------
        self.hr_main_menu = page.getByText("HR")
        
        #-----------------HR - Dashboard-------------------------------------------------------
        self.hr_menu_dashboard = page.locator("span").filter(has_text="Dashboard").first()        
        
        #--------------------HR-Employees------------------------------------------------------
        self.hr_menu_employees = page.locator(":text-is('Employees')")           
        
        #------------------------HR-Employees-Employees List---------------------------------------------
        self.hr_menu_emplist = page.get_by_text("Employees List")
        
        #----------------------HR-Add Employee------------------------------------------------
        self.hr_menu_add_employee = page.get_by_text("Add Employee")
        
        #---------------------------HR-Employees-Documents-------------------------------------
        self.hr_documents_menu = page.get_by_text("Documents")
        
        #--------------------------------HR-Attendance-------------------------------------------------
        self.hr_menu_attendance = page.locator("span").filter(has_text="Attendance").first()
        
        #---------------------HR- Employee Attendance------------------------------------------------------
        self.hr_employee_attendance = page.get_by_text("Employee Attendance")

        #-------------------------- HR-Weekoff Working---------------------------------------
        self.hr_weekoff_working = page.get_by_text("Weekoff Working")

        #---------------------- HR-Monthly Attendance---------------------------------------
        self.hr_monthly_attendance = page.get_by_text("Monthly Attendance")

        #----------------------------------------- HR-Attendance Correction-------------------------------
        self.hr_attendance_correction = page.get_by_text("Attendance Correction").last()

        #---------------------------- HR-Attendance Configuration------------------------------------------
        self.hr_attendance_config = page.get_by_text("Attendance Configuration")

        #----------------------- HR- View Roster------------------------------
        self.hr_view_roster = page.get_by_text("View Roster")

        #---------------- HR-Shifts-----------------------------------------
        self.hr_shifts_menu = page.get_by_text("Shifts")

        #----------------------------- HR-Attendance QR-----------------------------------
        self.hr_attendance_qr = page.get_by_text("Attendance QR")

        #---------------------------- HR-Gate Pass Approval------------------------------
        self.hr_gatepass_approval = page.get_by_text("Gate Pass Approval")
        
        #------------------ HR-Overtime Policies-------------------------------------
        self.hr_overtime_policies = page.get_by_text("Overtime Policies")
        
        #-------------------- HR-Overtime Assignments-----------------------------------
        self.hr_overtime_assignment = page.get_by_text("Overtime Assignments")
        
        #-------------HR- Overtime Approvals-----------------------
        self.hr_overtime_approval = page.get_by_text("Overtime Approvals")

        #-------------------------HR- Overtime Summary--------------------------------
        self.hr_overtime_summary = page.get_by_text("Overtime Summary")

        #------------------------ HR-Leave Management------------------------------------
        self.hr_leave_management = page.get_by_text("Leave Managment")

        #----------------------------- HR-Leave Types-----------------------------------
        self.hr_leave_types = page.get_by_text("Leave Types")

        #-------------------------------HR- Leave Increment Counter------------------------------
        self.hr_leave_inc_counter = page.get_by_text("Leave Increment Counter")

        #---------------------------HR- Leave Applications------------------------------------
        self.hr_leave_applications = page.get_by_text("Leave Applications")

        #---------------HR- Holidays-----------------------------------------------
        self.hr_holidays = page.get_by_text("Holidays", exact=True)

        #-------------------------------HR- Leave Balance------------------------------------
        self.hr_leave_balance = page.get_by_text("Leave Balance")

        #--------------------------HR- Comp Off Balance--------------------------------
        self.hr_comp_off_balance = page.get_by_text("Comp Off Balance").last()
        
        #----------------------- HR-Leave Allocation------------------------------
        self.hr_leave_allocation = page.get_by_text("Leave Allocation")

        #---------------------------- HR-Apply Leave-----------------------------
        self.hr_apply_leave = page.get_by_text("Apply Leave")

        #------------------ HR-Organization-----------------------------
        self.hr_organization = page.get_by_text("Organization")

        #------------------------ HR-Announcement-------------------------------
        self.hr_announcement = page.locator("span").filter(has_text="Announcement")

        #------------------HR- Employment Type----------------------------------
        self.hr_emplymnt_type = page.get_by_text("Employment Type")


        #==============================Payroll Module=========================================

        #-----------Payroll Management------------------------------------
        self.pr_payroll_management = page.getByText("Payroll Management")
        
        # Salary Structure
        self.pr_salary_structure = page.get_by_text("Salary Structure").last() 

        # EPF Setting
        self.pr_epf_setting = page.get_by_text("EPF Setting")

        # ESIC Setting
        self.pr_esic_setting = page.get_by_text("ESIC Setting")

        # Professional Tax
        self.pr_professional_tax = page.get_by_text("Professional Tax")

        # Pay Earning Elements
        self.pr_pay_earning_elements = page.get_by_text("Pay Earning Elements")

        # Deduction Elements
        self.pr_deduction_element = page.get_by_text("Deduction Elements")

        # Statutory Bonus
        self.pr_satutory_bonus = page.get_by_text("Statutory Bonus")

        # Gratuity Settings
        self.pr_gratuity_setting = page.get_by_text("Gratuity Settings")

        # Payroll Run
        self.pr_payroll_run = page.get_by_text("Payroll Run")

        # Bank Accounts
        self.pr_bank_account = page.get_by_text("Bank Accounts")
        
        
        
        #==============================Admin Module=========================================
        # Administrator
        self.admin_menu = page.get_by_text("Administrator")

        # Roles
        self.admin_roles = page.get_by_text("Roles")

        # Users
        self.admin_users = page.get_by_text("Users")

        # Branch
        self.admin_branch = page.get_by_text("Branch")

        # Department
        self.admin_department = page.get_by_text("Department")

        # Designation
        self.admin_designation = page.get_by_text("Designation")

        # Document Format
        self.admin_doc_format = page.get_by_text("Document Format")

        # GL Account
        self.admin_gl_account = page.get_by_text("GL Account")

        # Company Details
        self.admin_company_detail = page.get_by_text("Company Details")

        # Additional Configurations
        self.admin_addi_conf = page.get_by_text("Additional Configurations")
    
    
    
    #==============================Kiosk Module=========================================
    
        #Kiosk main menu
        self.kiosk = page.get_by_text("Kiosk")

        # Scanner
        self.kiosk_scanner = page.locator("span:has-text('Scanner')")

        # Leaves
        self.kiosk_leaves = page.locator("//a[@href='/kiosk/leaves']")

        # Gate Pass
        self.kiosk_gatepass = page.locator("//a[@href='/kiosk/gatepass']//span[contains(text(),'Gate Pass')]")


    
    
    
    
    #==============================Inventory Module=========================================
        # Inventory Management main menu
        self.inventory_mgmt = page.get_by_text("Inventory Management")

        # Items
        self.inventory_items = page.get_by_text("Items")

        # Stock
        self.inventory_stock = page.locator(":text-is('Stock')")

        # Stock Entry
        self.inv_st_stock_entry = page.get_by_text("Stock Entry")

        # Material Conversions
        self.inv_st_material_conv = page.get_by_text("Material Conversions")

        # Stock History
        self.inv_st_stock_history = page.get_by_text("Stock History")

        # Goods in Transit
        self.inv_st_goods_in_transit = page.get_by_text("Goods in Transit")

        # Stock Valuation
        self.inv_st_stock_valuation = page.get_by_text("Stock Valuation")

        # Rejected Stock
        self.inv_st_rejected_stock = page.get_by_text("Rejected Stock")

        # Cycle Count 
        self.inv_st_cycle_count = page.get_by_text("Cycle Count")

        # Purchase Order
        self.inv_purchase_Order = page.get_by_text("Purchase Order")

        # Customer Requirement
        self.inv_po_cust_req = page.get_by_text("Customer Requirement")

        # Request
        self.inv_po_request = page.locator(":text-is('Request')")

        # Order
        self.inv_po_order = page.locator("//a[@href='/inventory/purchaseorder']//span[contains(text(),'Order')]")

        # GRN
        self.inv_po_grn = page.get_by_text("GRN")

        # Bills
        self.inv_po_bills = page.get_by_text("Bills")

        # Bill Payments
        self.inv_po_bill_payment = page.get_by_text("Bill Payments")

        # Debit Notes
        self.inv_po_debit_note = page.get_by_text("Debit Notes")

        # Sales Order
        self.inv_sales_order = page.get_by_text("Sales Order")

        # Proforma Invoice
        self.inv_so_proforma = page.get_by_text("Proforma Invoice")

        # Order
        self.inv_so_order = page.locator("//a[@href='/inventory/saleorder']//span[contains(text(),'Order')]")

        # Delivery Challan
        self.inv_so_delivery_challan = page.locator("//span[normalize-space()='Delivery Challan']")

        # Material Outward
        self.inv_so_material_out = page.get_by_text("Material Outward")

        # Invoices
        self.inv_so_invoice = page.get_by_text("Invoices")

        # Payment Received
        self.inv_so_payment_received = page.get_by_text("Payment Received")

        # Credit Note
        self.inv_so_credit_note = page.get_by_text("Credit Note")

        # Pickup List
        self.inv_so_pickup_list = page.get_by_text("Pickup List")
            
        # Return & Replacement
        self.inv_return_replace = page.get_by_text("Return & Replacement")
        
        # Clients/Customers
        self.inv_client_cust = page.locator(":text('Clients/Customers')")
        
        # Accounts
        self.inv_account = page.locator("//span[normalize-space()='Accounts']")

        # Journal Entries
        self.inv_acc_journal_ent = page.locator(":text('Journal Entries')")

        # Day Book
        self.inv_acc_day_book = page.locator("//span[normalize-space()='Day Book']")

        # GL Ledger
        self.inv_acc_gl_ledger = page.locator("//span[normalize-space()='GL Ledger']")

        # Account Ledger
        self.inv_acc_acc_ledger = page.get_by_text("Account ledger")

        # Bank Book
        self.inv_acc_bank_book = page.get_by_text("Bank Book")
        
        # Financial Reports
        self.inv_financial_report = page.get_by_text("Financial Reports")

        # Trial Balance
        self.inv_fr_trial_balance = page.get_by_text("Trial Balance")

        # Profit & Loss
        self.inv_fr_profit_n_loss = page.get_by_text("Profit & Loss")

        # Balance Sheet
        self.inv_fr_balance_sheet = page.get_by_text("Balance Sheet")

        # Customer Statement
        self.inv_fr_cus_statement = page.get_by_text("Customer Statement")

        # Supplier Statement
        self.inv_fr_supplier_stat = page.locator("//a[@href='/inventory/supplier-statement']")
        
        # A/R Aging
        self.inv_fr_ar_aging = page.locator("//span[normalize-space()='A/R Aging']")

        # A/P Aging
        self.inv_fr_ap_aging = page.locator("//span[normalize-space()='A/P Aging']")

        # Commission Report
        self.inv_fr_comission_rep = page.locator("//span[normalize-space()='Commission Report']")

        # Sales Target
        self.inv_fr_sales_target = page.locator("//span[normalize-space()='Sales Targets']")

        # Sales Target Report
        self._inv_fr_sales_target_report = page.locator("//span[normalize-space()='Sales Target Report']")

        # Reconciliation
        self.inv_reconcialiation = page.locator("//span[normalize-space()='Reconciliation']")


        # Inventory-to-GL Reconciliation
        self.inv_reco_inven2glreco = page.locator("//span[normalize-space()='Inventory-to-GL Reconciliation']")

        # GR/IR Reconciliation
        self.inv_reco_grir_reco = page.locator("//span[normalize-space()='GR/IR Reconciliation']")

        # Bank Reconciliation
        self.inv_reco_bank_reco = page.locator("//span[normalize-space()='Bank Reconciliation']")

        # LCNRV Provision 
        self.inv_reco_lcnrv = page.locator("//span[normalize-space()='LCNRV Provision']")

        # GST Reports
        self.inv_gst_repo = page.locator("//span[normalize-space()='LCNRV Provision']")

        # GSTR-1
        self.inv_gst_gstr1 = page.locator("//span[normalize-space()='GSTR-1']")

        # GSTR-2B
        self.inv_gst_gstr2b = page.locator("//span[normalize-space()='GSTR-2B']")

        # GSTR-3B
        self.inv_gst_gstr3b = page.locator("//span[normalize-space()='GSTR-3B']")

        
        # Settings
        self.inv_settings = page.get_by_text("Settings", exact=True).nth(0)
        
        # Stores
        self.inv_sett_stores = page.get_by_text("Stores")

        # Measuring Unit
        self.inv__sett_measuring_unit = page.get_by_text("Measuring Unit")

        # Item Types
        self.inv_sett_item_types = page.get_by_text("Item Types")

        # HSN Codes
        self.inv_sett_hsn_code = page.get_by_text("HSN Codes")

        # Default
        self.inv_sett_default = page.get_by_text("Default")

        # Commission
        self.inv_sett_commission = page.locator(":text-is('Commission')")
        
    

    
    #==============================Lead Module=========================================
        # Lead Management main menu
        self.lead_management = page.get_by_text("Lead Management")

        # Leads
        self.lm_leads = page.get_by_text("Leads")

        # Lead Follow Ups
        self.lm_lead_follow_up = page.get_by_text("Lead Follow Ups")

        # Recent Follow Ups
        self.lm_recent_follow_up = page.get_by_text("Recent Follow Ups")

        # Lead Expenses
        self.lm_lead_exp = page.get_by_text("Lead Expenses")

        # Settings
        self.lm_settings = page.get_by_text("Settings", exact=True).nth(1)

        # Source
        self.lm_sett_source = page.get_by_text("Source")

        # Status
        self.lm_sett_status = page.locator(":text-is('Status')")

        # Sub Status
        self.lm_sett_sub_status = page.get_by_text("Sub Status")

        # Type 
        self.lm_sett_type = page.locator(":text-is('Type')")

        # Segment
        self.lm_sett_segment = page.get_by_text("Segment")

        # Class
        self.lm_sett_class = page.get_by_role("link", name="Class")

        # Lead Status
        self.lm_sett_lead_status = page.get_by_text("Lead Status")

        # City
        self.lm_sett_city = page.get_by_text("City")

        # Tehsils
        self.lm_sett_tehsil = page.get_by_text("Tehsils")

        # Priority
        self.lm_sett_priority = page.get_by_text("Priority")
       
    
    
    
    #==============================Sales Module=========================================
       
        # Sales Trips main menu
        self.sales_salestrip = page.get_by_text("Sales Trips")

        # Trips
        self.sales_trips = page.locator(":text-is('Trips')")

        # Day Map
        self.sales_day_map = page.get_by_role("link", name="Day Map")

        # Visits
        self.sales_visits = page.get_by_text("Visits")

        # Expenses
        self.sales_expen = page.locator(":text-is('Expenses')")
    
    
    
    
    
    
    #==============================Manufacturing Module=========================================
    
        # Manufacturing main menu
        # Dashboard
        # Planning
        # Forcast Entries
        # Production Schedule
        # Material Requests
        # Production
        # Bill Of Materials
        # Work Orders
        # Job Cards
        # Production Entries
        # Quality
        # QC Dashboard
        # QC Inbox
        # Inspections
        # NCR
        # Concessions
        # Release Status
        # Shop Floor
        # Workstations
        # Machines & Lines
        # Working Hours
        # Machine Load
        # Maintenance 
        # Downtime Logs
        # Masters
        # Operations
        # Inspection Plans
        # Defect Masters

    
    def emp_loyeeservice(self):
        self.employee_service.click()
       
    def emp_dashboard(self):
        self.dashboard_menu.click()

    def emp_profile(self):
        self.profile_menu.click()
    
    def emp_activity(self):
        self.activity.click()

    def emp_attendence(self):
        self.attendance_menu.click()
    
    def emp_leaves(self):
        self.leaves_menu.click()
    
    def emp_comp_off_balance(self):
        self.comp_off_menu().click()
    
    def emp_gatepass_menu(self):
        self.getepass_menu.click()
    
    def emp_shift(self):
        self.shift_menu.click()
    
    def emp_salarys_lip(self):
        self.salary_menu.click()

    def emp_salary_structure(self):
        self.salasy_structure_menu.click()

    #================HR module==============================
    def hr_menu(self):
        self.hr_main_menu.click()
    
    def hr_dashboard(self):
        self.hr_menu_dashboard.click()

    def hr_employees(self):
        self.hr_menu_employees.click()
    
    def hr_employees_list(self):
        self.hr_menu_emplist.click()

    def hr_add_employees(self):
        self.hr_menu_add_employee.click()
    
    def hr_documents(self):
        self.hr_documents_menu.click()

    def hr_attendance(self):
        self.hr_menu_attendance.click()

    def hr_emp_attendance(self):
        self.hr_employee_attendance.click()
    
    def hr_weekoff_working_menu(self):
        self.hr_weekoff_working.click()

    def hr_monthly_atten(self):
        self.hr_monthly_attendance.click()

    def hr_attend_correction(self):
        self.hr_attendance_correction.click()

    def hr_atten_conf(self):
        self.hr_attendance_config.click()

    def hr_view_rost(self):
        self.hr_view_roster.click()

    def hr_shifts(self):
        self.hr_shifts_menu.click()

    def hr_atten_qr(self):
        self.hr_attendance_qr.click()

    def hr_gp_approval(self):
        self.hr_gatepass_approval.click()

    def hr_ot_policy(self):
        self.hr_overtime_policies.click()

    def hr_ot_assignment(self):
        self.hr_overtime_assignment.click()

    def hr_ot_approvals(self):
        self.hr_overtime_approval.click()

    def hr_ot_summary(self):
        self.hr_overtime_summary.click()

#=============leave management
    def hr_leave_mgmt(self):
        self.hr_leave_management.click()

    def hr_leave_typ(self):
        self.hr_leave_types.click()

    def hr_leave_inc_coun(self):
        self.hr_leave_inc_counter.click()

    def hr_leave_app(self):
        self.hr_leave_applications.click()

    def hr_holiday(self):
        self.hr_holidays.click()

    def hr_leave_bal(self):
        self.hr_leave_balance.click()

    def hr_comp_off_bal(self):
        self.hr_comp_off_balance.click()

    def hr_leave_allo(self):
        self.hr_leave_allocation.click()

    def hr_aply_leave(self):
        self.hr_apply_leave.click()

    def hr_org(self):
        self.hr_organization.click()

    def hr_anno(self):
        self.hr_announcement.click()

    def hr_emp_type(self):
        self.hr_emplymnt_type.click()

#================== Payroll Management
    
    def pr_payroll_mgmt(self):
        self.pr_payroll_management.click()

    def pr_sal_struct(self):
        self.pr_salary_structure.click()

    def pr_epf_sett(self):
        self.pr_epf_setting.click()

    def pr_esic_sett(self):
        self.pr_esic_setting.click()
    
    def pr_pro_tax(self):
        self.pr_professional_tax.click()

    def pr_pay_earn_elemnt(self):
        self.pr_pay_earning_elements.click()

    def pr_deduc_elemnt(self):
        self.pr_deduction_element.click()

    def pr_satu_bonus(self):
        self.pr_satutory_bonus.click()

    def pr_grat_sett(self):
        self.pr_gratuity_setting.click()

    def pr_pay_run(self):
        self.pr_payroll_run.click()

    def pr_bank_acc(self):
        self.pr_bank_account.click()

#======== Admin

    def super_admin_menu(self):
        self.admin_menu.click()

    def adm_roles(self):
        self.admin_roles.click()

    def adm_users(self):
        self.admin_users.click()

    def adm_branch(self):
        self.admin_branch.click()

    def adm_depart(self):
        self.admin_department.click()

    def adm_desig(self):
        self.admin_designation.click()

    def adm_doc_format(self):
        self.admin_doc_format.click()

    def adm_gl_acc(self):
        self.admin_gl_account.click()

    def adm_comp_detail(self):
        self.admin_company_detail.click()

    def adm_addi_conf(self):
        self.admin_addi_conf.click()

#============Kiosk

    def ksk_menu(self):
        self.kiosk.click()

    def ksk_scan(self):
        self.kiosk_scanner.click()

    def ksk_leaves(self):
        self.kiosk_leaves.click()

    def ksk_gatepass(self):
        self.kiosk_gatepass.click()

#========Inventory Management

    def inv_mgmt_menu(self):
        self.inventory_mgmt.click()

    def inv_items(self):
        self.inventory_items.click()

    def inv_stock(self):
        self.inventory_stock.click()
    
    def inv_st_entry(self):
        self.inv_st_stock_entry.click() 
        
    def inv_st_m_conv(self):
        self.inv_st_material_conv.click()
    
    def inv_st_stock_hist(self):
        self.inv_st_stock_history.click()

    def inv_st_goods_in_tran(self):
        self.inv_st_goods_in_transit.click()

    def inv_st_stock_valu(self):
        self.inv_st_stock_valuation.click()

    def inv_st_rej_stock(self):
        self.inv_st_rejected_stock.click()

    def inv_st_cy_count(self):
        self.inv_st_cycle_count.click()

    def inv_po_main_menu(self):
        self.inv_purchase_Order.click()

    def inv_po_cu_req(self):
        self.inv_po_cust_req.click()

    def inv_po_req(self):
        self.inv_po_request.click()

    def inv_po_ordr(self):
        self.inv_po_order.click()
    
    def inv_po_gr(self):
        self.inv_po_grn.click()

    def inv_po_bils(self):
        self.inv_po_bills.click()

    def inv_po_bill_pay(self):
        self.inv_po_bill_pay.click()

    def inv_po_debit_not(self):
        self.inv_po_debit_note.click()

    def inv_so_main(self):
        self.inv_sales_order.click()

    def inv_so_pro_inv(self):
        self.inv_so_proforma.click()

    def inv_so_ordr(self):
        self.inv_so_order.click()

    def inv_so_deliv_challan(self):
        self.inv_so_delivery_challan.click()

    def inv_so_materi_out(self):
        self.inv_so_material_out.click()

    def inv_so_invo(self):
        self.inv_so_invoice.click()

    def inv_so_paymnt_received(self):
        self.inv_so_payment_received.click()

    def inv_so_crdt_note(self):
        self.inv_so_credit_note.click()

    def inv_so_pickup(self):
        self.inv_so_pickup_list.click()

    def inv_return_repl(self):
        self.inv_return_replace.click()

    def inv_clients(self):
        self.inv_client_cust.click()

        