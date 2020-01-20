"""
Models suitable for imports of Federal Audit Clearinghouse tables.
These models contain all columns used over the available period of record;
note that many columns are only used in certain calendar years.

See: https://harvester.census.gov/facdissem/PublicDataDownloads.aspx
"""

from django.db import models


class General(models.Model):
    # Use these fields to link tables- 4 digits
    audit_year = models.DecimalField(
        max_digits=4,
        decimal_places=0,
        help_text='Audit Year and DBKEY (database key) combined make up the primary key.'
    )
    # Use these fields to link tables- 1-6 digits
    dbkey = models.CharField(
        max_length=6,
        help_text='Audit Year and DBKEY (database key) combined make up the primary key.'
    )
    # Contact FAC for information
    type_of_entity = models.CharField(
        null=True,
        blank=True,
        max_length=1000,
        help_text='Contact FAC for information'
    )
    # mm/dd/yyyy
    fy_end_date = models.DateField(
        help_text='Fiscal Year End Date'
    )
    # single audit or program specific TODO
    audit_type = models.CharField(
        null=True,
        blank=True,
        max_length=32,
        help_text='Type of Audit',
    )
    # annual, biennial, or other (see next)
    period_covered = models.CharField(
        max_length=16,
        help_text='Audit Period Covered by Audit',
        choices=(
            ('A', 'Annual'),
            ('B', 'Biennial'),
            ('O', 'Other'),
        )
    )
    # number of months
    number_months = models.IntegerField(
        help_text="Number of Months Covered by the 'Other' Audit Period",
        null=True
    )
    # 9 digits
    ein = models.CharField(
        max_length=9,
        help_text='Primary Employer Identification Number'
    )
    # (Y)es / (N)o indicator
    multiple_eins = models.BooleanField(
        null=True,
        help_text='Identifies if the Submission Contains Multiple EINs'
    )
    # 3 digits
    ein_subcode = models.CharField(
        blank=True,
        null=True,
        max_length=3,
        help_text='Subcode assigned to the EIN'
    )
    # 9 digits
    duns = models.CharField(
        max_length=9,
        blank=True,
        null=True,
        help_text='Primary Data Universal Numbering System Number'
    )
    # (Y)es / (N)o indicator
    multiple_duns = models.BooleanField(
        null=True,
        help_text='Identifies if the Submission Contains Multiple DUNS'
    )
    # 70 characters max
    auditee_name = models.CharField(
        max_length=70,
        help_text='Name of the Auditee'
    )
    # 45 characters max
    street1 = models.CharField(
        blank=True,
        null=True,
        max_length=45,
        help_text='Auditee Street Address'
    )
    # 45 characters max
    street2 = models.CharField(
        blank=True,
        null=True,
        max_length=45,
        help_text='Auditee Street Address'
    )
    # 30 characters max
    city = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        help_text='Auditee City'
    )
    # 2 characters
    state = models.CharField(
        blank=True,
        null=True,
        max_length=2,
        help_text='Auditee State'
    )
    # 5 or 9 digits
    zipcode = models.CharField(
        blank=True,
        null=True,
        max_length=9,
        help_text='Auditee Zipcode'
    )
    # 50 characters max
    auditee_contact = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        help_text='Name of Auditee Contact'
    )
    # 40 characters max
    auditee_title = models.CharField(
        blank=True,
        null=True,
        max_length=40,
        help_text='Title of Auditee Contact'
    )
    # 10 digits
    auditee_phone = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        help_text='Auditee Phone Number'
    )
    # 10 digits
    auditee_fax = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        help_text='Auditee Fax Number (optional)'
    )
    # 60 characters max
    auditee_email = models.CharField(
        blank=True,
        null=True,
        max_length=60,
        help_text='Auditee Email address'
    )
    # mm/dd/yyyy
    auditee_date_signed = models.DateField(
        blank=True,
        null=True,
        help_text='Date of auditee signature'
    )
    # 70 characters max
    auditee_name_title = models.CharField(
        blank=True,
        null=True,
        max_length=70,
        help_text='Title of Auditee Certifying Official'
    )
    # 64 characters max
    cpa_firm_name = models.CharField(
        blank=True,
        null=True,
        max_length=64,
        help_text='CPA Firm Name'
    )
    # 9 digits
    auditor_ein = models.CharField(
        blank=True,
        null=True,
        max_length=9,
        help_text='CPA Firm EIN (only available for audit years 2013 and beyond)'
    )
    # 45 characters max
    cpa_street1 = models.CharField(
        blank=True,
        null=True,
        max_length=45,
        help_text='CPA Street Address'
    )
    # 45 characters max
    cpa_street2 = models.CharField(
        blank=True,
        null=True,
        max_length=45,
        help_text='CPA Street Address'
    )
    # 30 characters max
    cpa_city = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        help_text='CPA City'
    )
    # 2 characters
    cpa_state = models.CharField(
        blank=True,
        null=True,
        max_length=2,
        help_text='CPA State'
    )
    # 5 or 9 digits
    cpa_zipcode = models.CharField(
        blank=True,
        null=True,
        max_length=9,
        help_text='CPA Zip Code'
    )
    # 50 characters max
    cpa_contact = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        help_text='Name of CPA Contact'
    )
    # 40 characters max
    cpa_title = models.CharField(
        blank=True,
        null=True,
        max_length=40,
        help_text='Title of CPA Contact'
    )
    # 10 digits
    cpa_phone = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        help_text='CPA phone number'
    )
    # 10 digits
    cpa_fax = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        help_text='CPA fax number (optional)'
    )
    # 60 characters max
    cpa_email = models.CharField(
        blank=True,
        null=True,
        max_length=60,
        help_text='CPA email address'
    )
    # mm/dd/yyyy
    cpa_date_signed = models.DateField(
        blank=True,
        null=True,
        help_text='Date of CPA signature'
    )
    # (Y)es / (N)o indicator
    multiple_cpas = models.BooleanField(
        null=True,
        help_text='Identifies if the Submission Contains Multiple CPAs'
    )
    # COG_OVER - TODO inspect
    cog_over = models.CharField(
        blank=True,
        null=True,
        max_length=1,
        help_text='',
        choices=(
            ('C', 'Cognizant'),
            ('O', 'Oversight'),
        )
    )
    # 2 Digit Federal Agency prefix
    cog_agency = models.CharField(
        blank=True,
        null=True,
        max_length=2,
        help_text='Two digit Federal agency prefix of the cognizant agency'
    )
    # 2 Digit Federal Agency prefix
    oversight_agency = models.CharField(
        blank=True,
        null=True,
        max_length=2,
        help_text='Two digit Federal agency prefix of the oversight agency'
    )
    # U=Unqualifed, Q=Qualified, A=Adverse, D=Disclaimer
    typereport_fs = models.CharField(
        blank=True,
        null=True,
        max_length=1000,
        help_text='Type of Report Issued on the Financial Statements'
    )
    # Cash basis, Tax basis, Regulatory basis, Contractual basis, or Other basis
    sp_framework = models.CharField(
        blank=True,
        null=True,
        max_length=1000,
        help_text='Special Purpose Framework that was used as the basis of accounting'
    )
    # (Y)es / (N)o indicator
    sp_framework_required = models.BooleanField(
        null=True,
        help_text=(
            'Indicate whether or not the special purpose framework used '
            'as basis of accounting by state law or tribal law'
        )
    )
    # U=Unqualifed, Q=Qualified, A=Adverse, D=Disclaimer
    typereport_sp_framework = models.CharField(
        blank=True,
        null=True,
        max_length=16,
        help_text="The auditor's opinion on the special purpose framework",
        choices=(
            ('U', 'Unqualifed'),
            ('Q', 'Qualified'),
            ('A', 'Adverse'),
            ('D', 'Disclaimer')
       )
    )
    # (Y)es / (N)o indicator
    going_concern = models.BooleanField(
        null=True,
        help_text=(
            'Whether or not the audit contained a going concern paragraph on '
            'financial statements'
        )
    )
    # (Y)es / (N)o indicator
    reportable_condition = models.BooleanField(
        null=True,
        help_text=(
            'Whether or not the audit disclosed a reportable '
            'condition/significant deficiency on financial statements'
        )
    )
    # (Y)es / (N)o indicator
    material_weakness = models.BooleanField(
        null=True,
        help_text=(
            'Whether or not the audit disclosed any reportable '
            'condition/significant deficiency as a material weakness on '
            'financial statements'
        )
    )
    # (Y)es / (N)o indicator
    material_noncompliance = models.BooleanField(
        null=True,
        help_text=(
            'Whether or not the audit disclosed a material noncompliance on '
            'financial statements'
        )
    )
    # U=Unqualifed, Q=Qualified, A=Adverse, D=Disclaimer
    typereport_mp = models.CharField(
        blank=True,
        null=True,
        max_length=16,
        help_text='Type of Report Issued on the Major Program Compliance',
        choices=(
            ('U', 'Unqualifed'),
            ('Q', 'Qualified'),
            ('A', 'Adverse'),
            ('D', 'Disclaimer')
       )
    )
    # (Y)es / (N)o indicator
    dup_reports = models.BooleanField(
        null=True,
        help_text=(
            'Whether or not the financial statements include departments that '
            'have separate expenditures not included in this audit'
        )
    )
    # ($) 12 digits max
    dollar_threshold = models.CharField(
        blank=True,
        null=True,
        max_length=12,
        help_text='Dollar Threshold to distinguish between Type A and Type B programs.'
    )
    # (Y)es / (N)o indicator
    low_risk = models.BooleanField(
        null=True,
        help_text='Indicate whether or not the auditee qualified as a low-risk auditee'
    )
    # (Y)es / (N)o indicator
    reportable_condition_mp = models.BooleanField(
        null=True,
        help_text=(
            'Whether or not the audit disclosed a reportable '
            'condition/significant deficiency for any major program in the '
            'Schedule of Findings and Questioned Costs'
        )
    )
    # (Y)es / (N)o indicator
    material_weakness_mp = models.BooleanField(
        null=True,
        help_text=(
            'Indicate whether any reportable condition/signficant deficiency '
            'was disclosed as a material weakness for a major program in the '
            'Schedule of Findings and Questioned Costs'
        )
    )
    # (Y)es / (N)o indicator
    qcosts = models.BooleanField(
        null=True,
        help_text='Indicate whether or not the audit disclosed any known questioned costs.'
    )
    # (Y)es / (N)o indicator
    cy_findings = models.BooleanField(
        null=True,
        help_text=(
            'Indicate whether or not current year findings or prior year '
            'findings affecting direct funds were reported'
        )
    )
    # (Y)es / (N)o indicator
    py_schedule = models.BooleanField(
        null=True,
        help_text=(
            'Indicate whether or not the report includes a Summary Schedule of '
            'Prior Year Audit Findings'
        )
    )
    # 12 digits max
    tot_fed_expend = models.CharField(
        max_length=12,
        help_text='Total Federal Expenditures'
    )
    # mm/dd/yyyy
    date_firewall = models.DateField()
    # mm/dd/yyyy
    previous_date_firewall = models.DateField(
        blank=True,
        null=True
    )
    # (Y)es / (N)o indicator
    report_required = models.BooleanField(
        null=True,
        help_text='Distribution to Federal Agency required?'
    )
    # mm/dd/yyyy
    fac_accepted_date = models.DateField(
        blank=True,
        null=True,
        help_text=(
            'The most recent date an audit report was submitted to the FAC '
            'that passed FAC screening and was accepted as a valid OMB '
            'Circular A-133 report submission.'
        )
    )
    # 200 characters max
    cpa_foreign = models.CharField(
        blank=True,
        null=True,
        max_length=200,
        help_text='CPA Address (if international)'
    )
    # 6 characters max. TODO: something here is more than 6
    cpa_country = models.CharField(
        blank=True,
        null=True,
        max_length=16,
        help_text='CPA Country'
    )
