import streamlit as st
from fpdf import FPDF
import base64

# Create a class for PDF generation
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Bright Steps Therapy, LLC', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def generate_pdf(form_data):
    pdf = PDF()
    pdf.add_page()

    pdf.chapter_title("Child's Information")
    pdf.chapter_body(f"Child's Name: {form_data['child_name']}\nDate: {form_data['date']}")

    pdf.chapter_title("Required Documents")
    pdf.chapter_body("\n".join(form_data['required_docs']))

    pdf.chapter_title("Parent/Guardian/Sponsor Information")
    parent_info = (
        f"Mother's Name: {form_data['mother_name']}\n"
        f"Date of Birth: {form_data['mother_dob']}\n"
        f"Address: {form_data['mother_address']}\n"
        f"Phone: {form_data['mother_phone']}\n"
        f"Occupation/Employer: {form_data['mother_occupation']}\n"
        f"Highest Level of Education: {form_data['mother_education']}\n"
        f"Email: {form_data['mother_email']}\n\n"
        f"Father's Name: {form_data['father_name']}\n"
        f"Date of Birth: {form_data['father_dob']}\n"
        f"Address: {form_data['father_address']}\n"
        f"Phone: {form_data['father_phone']}\n"
        f"Occupation/Employer: {form_data['father_occupation']}\n"
        f"Highest Level of Education: {form_data['father_education']}\n"
        f"Email: {form_data['father_email']}\n"
    )
    pdf.chapter_body(parent_info)

    return pdf

def main():
    st.title("Bright Steps Therapy Form")

    # Form for child's information
    st.header("Child's Information")
    child_name = st.text_input("Child's Name")
    date = st.date_input("Date")

    # Form for required documents
    st.header("Required Documents")
    required_docs = st.multiselect(
        "Check all that apply:",
        [
            "Bright Steps Therapy patient packet completed to the best of your ability",
            "Physician's order",
            "Copy of your driver's license",
            "Copy of your child's insurance card",
            "Guardianship papers (if applicable)",
            "Copies of any prior PT / OT testing",
            "Copy of your child's IFSP or IEP (if applicable)",
            "Any other information that would be crucial to your child's evaluation and/or therapy"
        ]
    )

    # Form for parent's information
    st.header("Parent/Guardian/Sponsor Information")
    mother_name = st.text_input("Mother's Name")
    mother_dob = st.date_input("Mother's Date of Birth")
    mother_address = st.text_area("Mother's Address")
    mother_phone = st.text_input("Mother's Phone")
    mother_occupation = st.text_input("Mother's Occupation/Employer")
    mother_education = st.text_input("Mother's Highest Level of Education")
    mother_email = st.text_input("Mother's Email")

    father_name = st.text_input("Father's Name")
    father_dob = st.date_input("Father's Date of Birth")
    father_address = st.text_area("Father's Address")
    father_phone = st.text_input("Father's Phone")
    father_occupation = st.text_input("Father's Occupation/Employer")
    father_education = st.text_input("Father's Highest Level of Education")
    father_email = st.text_input("Father's Email")

    if st.button("Submit and Download"):
        form_data = {
            'child_name': child_name,
            'date': date,
            'required_docs': required_docs,
            'mother_name': mother_name,
            'mother_dob': mother_dob,
            'mother_address': mother_address,
            'mother_phone': mother_phone,
            'mother_occupation': mother_occupation,
            'mother_education': mother_education,
            'mother_email': mother_email,
            'father_name': father_name,
            'father_dob': father_dob,
            'father_address': father_address,
            'father_phone': father_phone,
            'father_occupation': father_occupation,
            'father_education': father_education,
            'father_email': father_email
        }

        pdf = generate_pdf(form_data)
        pdf_output = pdf.output(dest='S').encode('latin1')

        b64_pdf = base64.b64encode(pdf_output).decode('latin1')
        href = f'<a href="data:application/octet-stream;base64,{b64_pdf}" download="form.pdf">Download PDF</a>'
        st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
