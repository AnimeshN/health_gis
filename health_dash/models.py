from django.db import models
from django.contrib.gis.db import models
# Create your models here.

#table for alternate and allopathy hospitals
class TownhealthCentroid15Apr(models.Model):
	id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
	geom = models.PointField(blank=True, null=True)
	fid = models.IntegerField(blank=True, null=True)
	st_x = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	st_y = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	census_201 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	state_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	state_name = models.CharField(max_length=254, blank=True, null=True)
	district_c = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	district_n = models.CharField(max_length=254, blank=True, null=True)
	taluka_nam = models.CharField(max_length=254, blank=True, null=True)
	sub_distri = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	sub_dist_1 = models.CharField(max_length=254, blank=True, null=True)
	town_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	town_name = models.CharField(max_length=254, blank=True, null=True)
	tot_hh = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tot_pop = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tot_mpop = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tot_f_pop = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tot_sc_pop = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tot_sc_mpo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tot_sc_fpo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tot_st_pop = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tot_st_mpo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	cd_block_n = models.CharField(max_length=254, blank=True, null=True)
	no_hh_hl_h = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	sc_pop_201 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	st_pop_201 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	density_20 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	h_allo_tot = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	h_allo_bed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	h_allo_doc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	h_allo_din = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	h_allo_pm = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	h_allo_pin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	h_allo_dst = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	h_alt_tot = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	h_alt_bed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	h_alt_doc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	h_alt_din = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	h_alt_pm = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	h_alt_pin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	h_alt_dst = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	dispen_tot = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	dispen_bed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	dispen_doc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	dispen_din = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	dispen_pm = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	dispen_pin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	dispen_dst = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	famwel_tot = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	famwel_bed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	famwel_doc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	famwel_din = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	famwel_pm = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	famwel_pin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	famwel_dst = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mtrcld_tot = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mtrcld_bed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mtrcld_doc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mtrcld_din = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mtrcld_pm = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mtrcld_pin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mtrcld_dst = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mtrhom_tot = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mtrhom_bed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mtrhom_doc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mtrhom_din = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mtrhom_pm = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mtrhom_pin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mtrhom_dst = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tbhosp_tot = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tbhosp_bed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tbhosp_doc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tbhosp_din = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tbhosp_pm = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tbhosp_pin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tbhosp_dst = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	nrshom_tot = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	nrshom_bed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	nrshom_doc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	nrshom_din = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	nrshom_pm = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	nrshom_pin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	nrshom_dst = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	vetern_tot = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	vetern_bed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	vetern_doc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	vetern_din = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	vetern_pm = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	vetern_pin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	vetern_dst = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mobcln_tot = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mobcln_bed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mobcln_doc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mobcln_din = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mobcln_pm = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mobcln_pin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mobcln_dst = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	others_tot = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	others_bed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	others_doc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	others_din = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	others_pm = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	others_pin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	others_dst = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	nongov_out = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	nongov_oin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	nongov_hsp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	nongov_shp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
class Meta:
        managed = False
        db_table = 'townhealth_centroid_15apr'


#for chc and phc
class MahaVillageHealthCentroid29Mar(models.Model):
	id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
	geom = models.PointField(blank=True, null=True)
	fid = models.IntegerField(blank=True, null=True)
	st_x = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	st_y = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	census_201 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	state_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	state_name = models.CharField(max_length=254, blank=True, null=True)
	district_c = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	district_n = models.CharField(max_length=254, blank=True, null=True)
	taluka_cod = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	taluka_nam = models.CharField(max_length=254, blank=True, null=True)
	village_co = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	village_na = models.CharField(max_length=254, blank=True, null=True)
	cd_blk_cod = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	cd_blk_nam = models.CharField(max_length=254, blank=True, null=True)
	tot_hh = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tot_popu_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tot_popu_f = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tot_popu_s = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tot_popu_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tot_popu_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tot_popu_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tot_popu_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tot_popu_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	govt_medi_field = models.DecimalField(db_column='govt_medi_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
	govt_med_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	priv_medi_field = models.DecimalField(db_column='priv_medi_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
	priv_med_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	near_medi_field = models.CharField(db_column='near_medi_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
	near_med_1 = models.CharField(max_length=254, blank=True, null=True)
	near_med_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	chc_num = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	chc_doc_nu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	chc_doc_in = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	chc_param_field = models.DecimalField(db_column='chc_param_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
	chc_para_1 = models.CharField(max_length=254, blank=True, null=True)
	chc_distan = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	phc_num = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	phc_doc_nu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	phc_doc_in = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	phc_param_field = models.DecimalField(db_column='phc_param_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
	phc_para_1 = models.CharField(max_length=254, blank=True, null=True)
	phc_distan = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	phsubc_num = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	phsubc_doc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	phsubc_d_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	phsubc_par = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	phsubc_p_1 = models.CharField(max_length=254, blank=True, null=True)
	phsubc_dis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mch_num = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mch_doc_nu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mch_doc_in = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	mch_param_field = models.DecimalField(db_column='mch_param_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
	mch_para_1 = models.CharField(max_length=254, blank=True, null=True)
	mch_distan = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tbc_num = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tbc_doc_nu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tbc_doc_in = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	tbc_param_field = models.DecimalField(db_column='tbc_param_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
	tbc_para_1 = models.CharField(max_length=254, blank=True, null=True)
	tbc_distan = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	hosp_allo_field = models.DecimalField(db_column='hosp_allo_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
	hosp_all_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	hosp_all_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	hosp_all_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	hosp_all_4 = models.CharField(max_length=254, blank=True, null=True)
	hosp_all_5 = models.CharField(max_length=254, blank=True, null=True)
	hosp_alt_n = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	hosp_alt_d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	hosp_alt_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	hosp_alt_p = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	hosp_alt_2 = models.CharField(max_length=254, blank=True, null=True)
	hosp_all_d = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	dispensary = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	dispensa_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	dispensa_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	dispensa_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	dispensa_4 = models.CharField(max_length=254, blank=True, null=True)
	dispensa_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	fwc_num = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	fwc_tot_nu = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	fwc_doc_in = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	fwc_para_t = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	fwc_para_i = models.CharField(max_length=254, blank=True, null=True)
	fwc_dist_r = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	ngmf_out = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	ngmf_in_an = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	ngmf_char = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	ngmf_mbbs = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	ngmf_other = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	ngmf_no_de = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	ngmf_trad_field = models.DecimalField(db_column='ngmf_trad_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
	ngmf_shop = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	nfmf_other = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	nutri_cen_field = models.CharField(db_column='nutri_cen_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
	nutri_ce_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	angan = models.CharField(max_length=254, blank=True, null=True)
	angan_dist = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	other_nutr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	other_nu_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	asha = models.CharField(max_length=254, blank=True, null=True)
	asha_dist_field = models.DecimalField(db_column='asha_dist_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
	comm_cen_t = models.CharField(max_length=254, blank=True, null=True)
	comm_cen_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

class Meta:
        managed = False
        db_table = 'maha_village_health_centroid_29mar'


#dedicated covid hospitals
class CovidDedicatedHospitals(models.Model):
    geom = models.PointField(blank=True, null=True)
    sno = models.CharField(max_length=254, blank=True, null=True)
    state = models.CharField(max_length=254, blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    factly_nam = models.CharField(max_length=254, blank=True, null=True)
    category = models.CharField(max_length=254, blank=True, null=True)
    type = models.CharField(max_length=254, blank=True, null=True)
    facility_i = models.CharField(max_length=254, blank=True, null=True)
    iso_minus_field = models.CharField(db_column='iso_minus_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    iso_confm_field = models.CharField(db_column='iso_confm_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    iso_suspec = models.CharField(max_length=254, blank=True, null=True)
    o2suported = models.CharField(max_length=254, blank=True, null=True)
    total_icu = models.CharField(max_length=254, blank=True, null=True)
    ventilator = models.CharField(max_length=254, blank=True, null=True)
    o2_manifol = models.CharField(max_length=254, blank=True, null=True)
    ppe = models.CharField(max_length=254, blank=True, null=True)
    n95 = models.CharField(max_length=254, blank=True, null=True)
    bio_med_wa = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    result_num = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    formatted_field = models.CharField(db_column='formatted_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    place_id = models.CharField(max_length=254, blank=True, null=True)
    location_t = models.CharField(max_length=254, blank=True, null=True)
    latlong = models.CharField(max_length=254, blank=True, null=True)
    fid = models.CharField(max_length=254, blank=True, null=True)
    row_number = models.CharField(max_length=254, blank=True, null=True)
    layer = models.CharField(max_length=100, blank=True, null=True)
    path = models.CharField(max_length=254, blank=True, null=True)
    faclty_nam = models.CharField(max_length=254, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'covid_dedicated_hospitals'

#govt schools
class GovtSchools30April(models.Model):
    geom = models.MultiPointField(blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)
    sr_no = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name_of_at = models.CharField(max_length=254, blank=True, null=True)
    po = models.CharField(max_length=254, blank=True, null=True)
    udise_code = models.CharField(max_length=254, blank=True, null=True)
    name_of_sc = models.CharField(max_length=254, blank=True, null=True)
    village = models.CharField(max_length=254, blank=True, null=True)
    village_ce = models.CharField(max_length=254, blank=True, null=True)
    remarks = models.CharField(max_length=254, blank=True, null=True)
    taluka = models.CharField(max_length=254, blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    school_sta = models.CharField(max_length=254, blank=True, null=True)
    school_end = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'govt_schools_30april'

#aided schools
class AidedSchools30April(models.Model):
    geom = models.MultiPointField(blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)
    udise = models.CharField(max_length=254, blank=True, null=True)
    school_nam = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    village = models.CharField(max_length=254, blank=True, null=True)
    taluka = models.CharField(max_length=254, blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    po = models.CharField(max_length=254, blank=True, null=True)
    atc = models.CharField(max_length=254, blank=True, null=True)
    student_co = models.CharField(max_length=254, blank=True, null=True)
    student_ca = models.CharField(max_length=254, blank=True, null=True)
    type = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aided_schools_30april'

#bifoculs
class InstBifocals4May2020(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    geom = models.PointField(blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)
    inst_ctgry = models.CharField(max_length=254, blank=True, null=True)
    othr_ctgry = models.CharField(max_length=254, blank=True, null=True)
    dvet_code = models.CharField(max_length=254, blank=True, null=True)
    inst_name = models.CharField(max_length=254, blank=True, null=True)
    inst_type = models.CharField(max_length=254, blank=True, null=True)
    location = models.CharField(max_length=254, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    altitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    l_precisio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    area_name = models.CharField(max_length=254, blank=True, null=True)
    city_vlg_t = models.CharField(max_length=254, blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    taluka = models.CharField(max_length=254, blank=True, null=True)
    pincode = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    images = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inst_bifocals_4may2020'

#vti
class InstVti4May2020(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    geom = models.PointField(blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)
    inst_ctgry = models.CharField(max_length=254, blank=True, null=True)
    othr_ctgry = models.CharField(max_length=254, blank=True, null=True)
    dvet_code = models.CharField(max_length=254, blank=True, null=True)
    inst_name = models.CharField(max_length=254, blank=True, null=True)
    inst_type = models.CharField(max_length=254, blank=True, null=True)
    location = models.CharField(max_length=254, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    altitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    l_precisio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    area_name = models.CharField(max_length=254, blank=True, null=True)
    city_vlg_t = models.CharField(max_length=254, blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    taluka = models.CharField(max_length=254, blank=True, null=True)
    pincode = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    images = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inst_vti_4may2020'


#iti
class TotIti13Apr2020(models.Model):
    geom = models.PointField(blank=True, null=True)
    fid = models.IntegerField(blank=True, null=True)
    dvet_inst_field = models.DecimalField(db_column='dvet_inst_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
    inst_name = models.CharField(max_length=254, blank=True, null=True)
    alias_name = models.CharField(max_length=254, blank=True, null=True)
    inst_type = models.CharField(max_length=254, blank=True, null=True)
    category = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    city_vlg_t = models.CharField(max_length=254, blank=True, null=True)
    pincode = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    taluka = models.CharField(max_length=254, blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    region = models.CharField(max_length=254, blank=True, null=True)
    location = models.CharField(max_length=254, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    trade_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    trade_name = models.CharField(max_length=254, blank=True, null=True)
    tot_seat_i = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    no_of_shif = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    infra_fclt = models.CharField(max_length=254, blank=True, null=True)
    no_of_facu = models.CharField(max_length=254, blank=True, null=True)
    inst_head = models.CharField(max_length=254, blank=True, null=True)
    inst_conta = models.CharField(max_length=254, blank=True, null=True)
    inst_email = models.CharField(max_length=254, blank=True, null=True)
    inst_url = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tot_iti_13apr2020'
