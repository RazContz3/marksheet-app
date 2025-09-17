from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd
import os
import sqlite3
import json

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'marks.db')
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# Sheet-like data entry route
@app.route('/data_entry')
def data_entry():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql('SELECT * FROM final_clean_10S1_Marks_Sheet_2025', conn)
    conn.close()
    columns = [{'title': col, 'field': col} for col in df.columns]
    data = df.to_dict(orient='records')
    return render_template('data_entry.html', columns=columns, data=data)

# API endpoint to save edited data
@app.route('/api/save_data', methods=['POST'])
def save_data():
    rows = request.json.get('data', [])
    if not rows:
        return jsonify({'status': 'error', 'message': 'No data received'})
    conn = sqlite3.connect(DB_PATH)
    df = pd.DataFrame(rows)
    df.to_sql('final_clean_10S1_Marks_Sheet_2025', conn, if_exists='replace', index=False)
    conn.close()
    return jsonify({'status': 'success'})

# Utility: Import CSVs to SQLite (run once)
def import_csvs_to_db():
    conn = sqlite3.connect(DB_PATH)
    for fname in os.listdir(DATA_DIR):
        if fname.endswith('.csv'):
            df = pd.read_csv(os.path.join(DATA_DIR, fname))
            table_name = os.path.splitext(fname)[0]
            df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()


if not os.path.exists(DB_PATH):
    import_csvs_to_db()

# Dashboard route
@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql('SELECT * FROM final_clean_10S1_Marks_Sheet_2025', conn)
    conn.close()
    # Pass/Fail logic
    main_subjects = ['SINHALA','ENGLISH','MATHS','HISTORY','SCIENCE','BI (BS/Civics/Tamil)']
    def is_pass(row):
        return all(pd.to_numeric(row[subj], errors='coerce') >= 35 for subj in main_subjects if row[subj] not in ('', None))
    df['Result'] = df.apply(is_pass, axis=1)
    passed = df[df['Result'] == True]
    failed = df[df['Result'] == False]
    # Special attention
    def is_may_be_pass(row):
        for subj in main_subjects:
            val = row[subj]
            try:
                mark = float(val)
                if 20 <= mark < 35:
                    return True
            except:
                continue
        return False
    def is_withdrawn(row):
        return any(str(row[subj]).strip().upper() == 'W' for subj in main_subjects)
    may_be_pass = df[df.apply(is_may_be_pass, axis=1)]
    withdrawn = df[df.apply(is_withdrawn, axis=1)]
    # Basket subjects
    basket_subjects = ['BS', 'Civics', 'Tamil', 'Geography', 'Art', 'Dancing', 'E Music', 'W Music', 'Drama', 'E Lit.', 'ICT', 'HSc', 'Media']
    basket_labels = json.dumps(basket_subjects)
    basket_averages = json.dumps([
        round(pd.to_numeric(df[subj], errors='coerce').mean(), 2) if subj in df.columns else 0 for subj in basket_subjects
    ])
    stats = {
        'total_students': len(df),
        'pass_rate': round(len(passed) / len(df) * 100, 2) if len(df) > 0 else 0,
        'fail_rate': round(len(failed) / len(df) * 100, 2) if len(df) > 0 else 0,
        'special_attention': len(may_be_pass) + len(withdrawn),
        'passed': len(passed),
        'failed': len(failed)
    }
    return render_template('dashboard.html', stats=stats, basket_labels=basket_labels, basket_averages=basket_averages)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def students():
    conn = sqlite3.connect(DB_PATH)
    students = pd.read_sql('SELECT * FROM final_clean_10S1_Marks_Sheet_2025', conn)
    conn.close()
    return render_template('students.html', students=students.to_dict(orient='records'))

# Add more routes for reports, search, export, etc.

# Pass/Fail Report
@app.route('/report/basket')
def report_basket():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql('SELECT * FROM final_clean_10S1_Marks_Sheet_2025', conn)
    conn.close()
    basket_subjects = ['BS', 'Civics', 'Tamil', 'Geography', 'Art', 'Dancing', 'E Music', 'W Music', 'Drama', 'E Lit.', 'ICT', 'HSc', 'Media']
    # Prepare summary for each basket subject
    basket_summary = {}
    for subj in basket_subjects:
        scores = pd.to_numeric(df[subj], errors='coerce')
        basket_summary[subj] = {
            'count': scores.count(),
            'average': round(scores.mean(), 2) if scores.count() > 0 else None,
            'min': scores.min() if scores.count() > 0 else None,
            'max': scores.max() if scores.count() > 0 else None
        }
    return render_template('basket_report.html', basket_summary=basket_summary)

    # PDF Export for Basket Subjects Report
    @app.route('/report/basket/pdf')
    def export_basket_pdf():
        import pdfkit
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql('SELECT * FROM final_clean_10S1_Marks_Sheet_2025', conn)
        conn.close()
        basket_subjects = ['BS', 'Civics', 'Tamil', 'Geography', 'Art', 'Dancing', 'E Music', 'W Music', 'Drama', 'E Lit.', 'ICT', 'HSc', 'Media']
        basket_summary = {}
        for subj in basket_subjects:
            scores = pd.to_numeric(df[subj], errors='coerce')
            basket_summary[subj] = {
                'count': scores.count(),
                'average': round(scores.mean(), 2) if scores.count() > 0 else None,
                'min': scores.min() if scores.count() > 0 else None,
                'max': scores.max() if scores.count() > 0 else None
            }
        html = render_template('basket_report_pdf.html', basket_summary=basket_summary)
        pdf = pdfkit.from_string(html, False, options={"enable-local-file-access": ""})
        return (pdf, 200, {'Content-Type': 'application/pdf', 'Content-Disposition': 'attachment; filename=basket_report.pdf'})
@app.route('/report/passfail')
def report_passfail():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql('SELECT * FROM final_clean_10S1_Marks_Sheet_2025', conn)
    conn.close()
    # Define pass criteria (e.g., 35+ in all main subjects)
    main_subjects = ['SINHALA','ENGLISH','MATHS','HISTORY','SCIENCE','BI (BS/Civics/Tamil)']
    def is_pass(row):
        return all(pd.to_numeric(row[subj], errors='coerce') >= 35 for subj in main_subjects if row[subj] not in ('', None))
    df['Result'] = df.apply(is_pass, axis=1)
    passed = df[df['Result'] == True]
    failed = df[df['Result'] == False]
    return render_template('passfail_report.html', passed=passed.to_dict(orient='records'), failed=failed.to_dict(orient='records'))

    # PDF Export for Pass/Fail Report
    @app.route('/report/passfail/pdf')
    def export_passfail_pdf():
        import pdfkit
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql('SELECT * FROM final_clean_10S1_Marks_Sheet_2025', conn)
        conn.close()
        main_subjects = ['SINHALA','ENGLISH','MATHS','HISTORY','SCIENCE','BI (BS/Civics/Tamil)']
        def is_pass(row):
            return all(pd.to_numeric(row[subj], errors='coerce') >= 35 for subj in main_subjects if row[subj] not in ('', None))
        df['Result'] = df.apply(is_pass, axis=1)
        passed = df[df['Result'] == True]
        failed = df[df['Result'] == False]
        html = render_template('passfail_report_pdf.html', passed=passed.to_dict(orient='records'), failed=failed.to_dict(orient='records'))
        pdf = pdfkit.from_string(html, False, options={"enable-local-file-access": ""})
        return (pdf, 200, {'Content-Type': 'application/pdf', 'Content-Disposition': 'attachment; filename=passfail_report.pdf'})

# Term-wise Summary Report
@app.route('/report/term_summary')
def report_term_summary():
    conn = sqlite3.connect(DB_PATH)
    # Find all tables for terms (assuming naming convention: final_clean_*)
    tables = []
    for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table'"):
        if row[0].startswith('final_clean_'):
            tables.append(row[0])
    term_stats = []
    for table in tables:
        df = pd.read_sql(f'SELECT * FROM {table}', conn)
        stat = {
            'term': table.replace('final_clean_', '').replace('_', ' '),
            'student_count': len(df),
            'average_total': round(pd.to_numeric(df['TOTAL'], errors='coerce').mean(), 2),
            'max_total': pd.to_numeric(df['TOTAL'], errors='coerce').max(),
            'min_total': pd.to_numeric(df['TOTAL'], errors='coerce').min()
        }
        term_stats.append(stat)
    conn.close()
    return render_template('term_summary_report.html', term_stats=term_stats)

    # PDF Export for Term-wise Summary Report
    @app.route('/report/term_summary/pdf')
    def export_term_summary_pdf():
        import pdfkit
        conn = sqlite3.connect(DB_PATH)
        tables = []
        for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table'"):
            if row[0].startswith('final_clean_'):
                tables.append(row[0])
        term_stats = []
        for table in tables:
            df = pd.read_sql(f'SELECT * FROM {table}', conn)
            stat = {
                'term': table.replace('final_clean_', '').replace('_', ' '),
                'student_count': len(df),
                'average_total': round(pd.to_numeric(df['TOTAL'], errors='coerce').mean(), 2),
                'max_total': pd.to_numeric(df['TOTAL'], errors='coerce').max(),
                'min_total': pd.to_numeric(df['TOTAL'], errors='coerce').min()
            }
            term_stats.append(stat)
        conn.close()
        html = render_template('term_summary_report_pdf.html', term_stats=term_stats)
        pdf = pdfkit.from_string(html, False, options={"enable-local-file-access": ""})
        return (pdf, 200, {'Content-Type': 'application/pdf', 'Content-Disposition': 'attachment; filename=term_summary_report.pdf'})

    # Special Attention List Report
    @app.route('/report/special_attention')
    def report_special_attention():
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql('SELECT * FROM final_clean_10S1_Marks_Sheet_2025', conn)
        conn.close()
        main_subjects = ['SINHALA','ENGLISH','MATHS','HISTORY','SCIENCE','BI (BS/Civics/Tamil)']
        # May Be Pass: 20-34 in any main subject
        def is_may_be_pass(row):
            for subj in main_subjects:
                val = row[subj]
                try:
                    mark = float(val)
                    if 20 <= mark < 35:
                        return True
                except:
                    continue
            return False
        # Withdrawn: 'W' in any main subject
        def is_withdrawn(row):
            return any(str(row[subj]).strip().upper() == 'W' for subj in main_subjects)
        may_be_pass = df[df.apply(is_may_be_pass, axis=1)]
        withdrawn = df[df.apply(is_withdrawn, axis=1)]
        return render_template('special_attention_report.html', may_be_pass=may_be_pass.to_dict(orient='records'), withdrawn=withdrawn.to_dict(orient='records'))

        # PDF Export for Special Attention Report
        @app.route('/report/special_attention/pdf')
        def export_special_attention_pdf():
            import pdfkit
            conn = sqlite3.connect(DB_PATH)
            df = pd.read_sql('SELECT * FROM final_clean_10S1_Marks_Sheet_2025', conn)
            conn.close()
            main_subjects = ['SINHALA','ENGLISH','MATHS','HISTORY','SCIENCE','BI (BS/Civics/Tamil)']
            def is_may_be_pass(row):
                for subj in main_subjects:
                    val = row[subj]
                    try:
                        mark = float(val)
                        if 20 <= mark < 35:
                            return True
                    except:
                        continue
                return False
            def is_withdrawn(row):
                return any(str(row[subj]).strip().upper() == 'W' for subj in main_subjects)
            may_be_pass = df[df.apply(is_may_be_pass, axis=1)]
            withdrawn = df[df.apply(is_withdrawn, axis=1)]
            html = render_template('special_attention_report_pdf.html', may_be_pass=may_be_pass.to_dict(orient='records'), withdrawn=withdrawn.to_dict(orient='records'))
            pdf = pdfkit.from_string(html, False, options={"enable-local-file-access": ""})
            return (pdf, 200, {'Content-Type': 'application/pdf', 'Content-Disposition': 'attachment; filename=special_attention_report.pdf'})

        # Student Detail Report
        @app.route('/student/<int:student_id>')
        def student_detail(student_id):
            conn = sqlite3.connect(DB_PATH)
            df = pd.read_sql('SELECT * FROM final_clean_10S1_Marks_Sheet_2025', conn)
            conn.close()
            student = df[df['No'] == student_id]
            if student.empty:
                return render_template('student_detail.html', student=None)
            return render_template('student_detail.html', student=student.iloc[0].to_dict())

            # PDF Export for Student Detail Report
            @app.route('/student/<int:student_id>/pdf')
            def export_student_detail_pdf(student_id):
                import pdfkit
                conn = sqlite3.connect(DB_PATH)
                df = pd.read_sql('SELECT * FROM final_clean_10S1_Marks_Sheet_2025', conn)
                conn.close()
                student = df[df['No'] == student_id]
                if student.empty:
                    html = render_template('student_detail_pdf.html', student=None)
                else:
                    html = render_template('student_detail_pdf.html', student=student.iloc[0].to_dict())
                pdf = pdfkit.from_string(html, False, options={"enable-local-file-access": ""})
                return (pdf, 200, {'Content-Type': 'application/pdf', 'Content-Disposition': f'attachment; filename=student_{student_id}_detail.pdf'})

if __name__ == '__main__':
    app.run(debug=True)
