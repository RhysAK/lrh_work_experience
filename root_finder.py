#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:12:10 2024

@author: rhysarmahkwantreng
"""
import xml.etree.ElementTree as ET
import pandas as pd

filepath = '/Users/rhysarmahkwantreng/Documents/LRH Code/SPTS0822_D052_20240809_223007_0.xml'
output_csv_path = '/Users/rhysarmahkwantreng/Documents/DTCC.csv'


def extract_data(filepath):
    # Parse the XML file
    tree = ET.parse(filepath)
    root = tree.getroot()

    # Register namespaces
    ns = {
        'head': 'urn:iso:std:iso:20022:tech:xsd:head.003.001.01',
        'auth': 'urn:iso:std:iso:20022:tech:xsd:auth.052.001.02'
    }

    # Initialize lists to store the extracted data
    tech_rcrd_id_data = []
    rptg_dt_tm_data = []
    rptg_ctr_pty_lei_data = []
    rpt_submitg_ntty_lei_data = []
    fi_clssfctn_data = []
    clssfctn_data = []
    ntty_rspnsbl_for_rpt_data = []
    lgl_lei_data = []
    
    

    # Extract TechRcrdId elements
    for tech_rcrd_id in root.findall('.//auth:TechRcrdId', ns):
        if tech_rcrd_id is not None:
            tech_rcrd_id_data.append(tech_rcrd_id.text)
            
    #Extract time stamp data
    for ctr_pty_data in root.findall('.//auth:CtrPtySpcfcData', ns):
        time = ctr_pty_data.find('.//auth:RptgDtTm', ns)
        if time is not None:
           rptg_dt_tm_data.append(time.text)

    # Extract reporting counterparty elements
    for rptg_ctr_pty in root.findall('.//auth:RptgCtrPty', ns):
        lei = rptg_ctr_pty.find('.//auth:Id/auth:LEI', ns)
        if lei is not None:
            rptg_ctr_pty_lei_data.append(lei.text)

    # Extract report submitting entity elements 
    for rpt_submitg_ntty in root.findall('.//auth:RptSubmitgNtty', ns):
        lei = rpt_submitg_ntty.find('.//auth:LEI', ns)
        if lei is not None:
            rpt_submitg_ntty_lei_data.append(lei.text)
            
     # Extract Nature of reporting counterparty elements 
    for ntr in root.findall('.//auth:RptgCtrPty/auth:Ntr/auth:FI/auth:Clssfctn', ns):
        if ntr is not None:
            fi_clssfctn_data.append(ntr.text) 
    
    # Extract Sector counterparty type 
    for Ntr in root.findall('.//auth:Ntr', ns):
        tag_names = [child.tag.split('}')[-1] for child in Ntr]
        tag_names_st = ' '.join(tag_names)  
        clssfctn_data.append(tag_names_st)
    
    # Extract entity responsible for the report data 
    for ntty_rspnsbl_for_rpt in root.findall('.//auth:NttyRspnsblForRpt', ns):
       lei = ntty_rspnsbl_for_rpt.find('.//auth:LEI', ns)
       if lei is not None:
           ntty_rspnsbl_for_rpt_data.append(lei.text)
           

    # Find and extract LEI elements under the Lgl tag
    for lgl in root.findall('.//auth:Lgl', ns):
       lei = lgl.find('.//auth:LEI', ns)
       if lei is not None:
          lgl_lei_data.append(lei.text)
                
    
 
    # Create a pandas DataFrame from the lists
    df = pd.DataFrame({
        'Technical Record ID': tech_rcrd_id_data,
        'Reporting Time Stamp': rptg_dt_tm_data,
        'Reporting Counterparty ': rptg_ctr_pty_lei_data,
        'Report Submitting Entity': rpt_submitg_ntty_lei_data,
        'Nature of Reporting Counterparty': fi_clssfctn_data,
        'Sector of Reporting Counterparty': clssfctn_data,
        'Entity Responsible for the Report': ntty_rspnsbl_for_rpt_data,
        'Other Counterparty':lgl_lei_data
        
    })

    return df

# Extract data from the XML file and create a DataFrame
df = extract_data(filepath)

# Write the DataFrame to a CSV file
df.to_csv(output_csv_path, index=False)

print(f"Data successfully written to {output_csv_path}")