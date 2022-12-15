from page.show_project.new_method_page import New_Method_Page


class Deal_With_Method:
    """
    新建方法页面 - 参数填入
    """

    def __init__(self, driver):
        self.driver = driver
        self.new_method_page = New_Method_Page(self.driver)

    def save_alert(self, deal_with_name):
        """
        保存处理方法弹窗
        :param deal_with_name:
        :return:
        """
        self.new_method_page.click_new_method_save_button()
        self.new_method_page.input_alert_save_deal_with_method_input(deal_with_name)
        self.new_method_page.click_alert_save_deal_with_method_confirm_button()

    def global_integration(self, peak_with, slope):
        """
        全局积分 参数填入
        :param peak_with:
        :param slope:
        :return:
        """
        self.new_method_page.input_peak_width(peak_with)
        self.new_method_page.input_slope(slope)

    def subsection_integration(self, order_start_time, order_end_time, order_peak_width, order_slope):
        """
        分段积分-分段积分参数 参数填入
        :param order_start_time:
        :param order_end_time:
        :param order_peak_width:
        :param order_slope:
        :return:
        """
        self.new_method_page.click_add_second_order_integralevent_button()
        self.new_method_page.input_subsection_order_start_time_param(order_start_time)
        self.new_method_page.input_subsection_order_end_time_param(order_end_time)
        self.new_method_page.input_subsection_order_peak_width_param(order_peak_width)
        self.new_method_page.input_subsection_order_slope_param(order_slope)

    def constituent(self, constituent_name, constituent_param, constituent_time):
        """
        组分 参数填入
        :param constituent_name:
        :param constituent_param:
        :param constituent_time:
        :return:
        """
        self.new_method_page.click_open_constituent_tab()
        self.new_method_page.click_open_constituent_add_button_button()
        self.new_method_page.input_open_constituent_name_param(constituent_name)
        self.new_method_page.input_open_constituent_param(constituent_param)
        self.new_method_page.input_open_constituent_time_param(constituent_time)

    def system_adaptability(self, empty_volume_time, suitparams_column_length, baseline_noise_max,
                            baseline_drift_max, baseline_running_time, baseline_start_time,
                            baseline_end_time, computer_baseline_start_time,
                            computer_baseline_end_time, pda_slice_width):
        """
        系统适应性 参数填入
        :param empty_volume_time:
        :param suitparams_column_length:
        :param baseline_noise_max:
        :param baseline_drift_max:
        :param baseline_running_time:
        :param baseline_start_time:
        :param baseline_end_time:
        :param computer_baseline_start_time:
        :param computer_baseline_end_time:
        :param pda_slice_width:
        :return:
        """
        self.new_method_page.click_open_system_adaptation_button()
        self.new_method_page.input_open_system_adaptation_empty_volume_time_param(empty_volume_time)
        self.new_method_page.input_open_system_adaptation_suitparams_column_length_param(suitparams_column_length)
        self.new_method_page.input_open_system_adaptation_baseline_noise_max_param(baseline_noise_max)
        self.new_method_page.input_open_system_adaptation_baseline_drift_max_param(baseline_drift_max)
        self.new_method_page.input_open_system_adaptation_baseline_running_time_param(baseline_running_time)
        self.new_method_page.input_open_system_adaptation_baseline_start_time_param(baseline_start_time)
        self.new_method_page.input_open_system_adaptation_baseline_end_time_param(baseline_end_time)
        self.new_method_page.input_open_system_adaptation_computer_baseline_start_time_param(
            computer_baseline_start_time)
        self.new_method_page.input_open_system_adaptation_computer_baseline_end_time_param(computer_baseline_end_time)
        self.new_method_page.input_open_system_adaptation_pda_slice_width_param(pda_slice_width)

    def pda(self, wavelength, wavelength_start, wavelength_end, spectral_library_name):
        """
        PDA 参数填入
        :param wavelength:
        :param wavelength_start:
        :param wavelength_end:
        :param spectral_library_name:
        :return:
        """
        self.new_method_page.click_open_pda_button()
        self.new_method_page.input_open_pda_wavelength_param(wavelength)
        self.new_method_page.input_open_pda_wavelength_start_param(wavelength_start)
        self.new_method_page.input_open_pda_wavelength_end_param(wavelength_end)
        self.new_method_page.input_open_pda_spectral_library_param()
        self.new_method_page.click_open_pda_spectral_library_name(spectral_library_name)

    def single_global(self, peak_with, slope, deal_with_name):
        """
        全局积分
        :return:
        """
        self.global_integration(peak_with, slope)
        self.save_alert(deal_with_name)

    def global_constituent(self, peak_with, slope, constituent_name, constituent_param, constituent_time,
                           deal_with_name):
        """
        全局积分 + 组分
        :return:
        """
        self.global_integration(peak_with, slope)
        self.constituent(constituent_name, constituent_param, constituent_time)
        self.save_alert(deal_with_name)

    def global_constituent_system(self, peak_with, slope, constituent_name,
                                  constituent_param, constituent_time, empty_volume_time, suitparams_column_length,
                                  baseline_noise_max,
                                  baseline_drift_max, baseline_running_time, baseline_start_time,
                                  baseline_end_time, computer_baseline_start_time,
                                  computer_baseline_end_time, pda_slice_width, deal_with_name):
        """
        全局积分 + 组分 + 系统适应性
        :return:
        """
        self.global_integration(peak_with, slope)
        self.constituent(constituent_name, constituent_param, constituent_time)
        self.system_adaptability(empty_volume_time, suitparams_column_length, baseline_noise_max,
                                 baseline_drift_max, baseline_running_time, baseline_start_time,
                                 baseline_end_time, computer_baseline_start_time,
                                 computer_baseline_end_time, pda_slice_width)
        self.save_alert(deal_with_name)

    def global_constituent_system_pda(self, peak_with, slope, constituent_name,
                                      constituent_param, constituent_time, empty_volume_time, suitparams_column_length,
                                      baseline_noise_max,
                                      baseline_drift_max, baseline_running_time, baseline_start_time,
                                      baseline_end_time, computer_baseline_start_time,
                                      computer_baseline_end_time, pda_slice_width, deal_with_name,
                                      wavelength, wavelength_start, wavelength_end, spectral_library_name):
        """
        全局积分 + 组分 + 系统适应性 + pda
        :return:
        """
        self.global_integration(peak_with, slope)
        self.constituent(constituent_name, constituent_param, constituent_time)
        self.system_adaptability(empty_volume_time, suitparams_column_length, baseline_noise_max,
                                 baseline_drift_max, baseline_running_time, baseline_start_time,
                                 baseline_end_time, computer_baseline_start_time,
                                 computer_baseline_end_time, pda_slice_width)
        self.pda(wavelength, wavelength_start, wavelength_end, spectral_library_name)
        self.save_alert(deal_with_name)

    def single_subsection(self, order_start_time, order_end_time, order_peak_width, order_slope
                          , deal_with_name):
        """
        分段积分
        :return:
        """
        self.subsection_integration(order_start_time, order_end_time, order_peak_width, order_slope)
        self.save_alert(deal_with_name)

    def subsection_constituent(self, order_start_time, order_end_time, order_peak_width, order_slope
                               , constituent_name, constituent_param, constituent_time, deal_with_name):
        """
        分段积分 + 组分
        :return:
        """
        self.subsection_integration(order_start_time, order_end_time, order_peak_width, order_slope)
        self.constituent(constituent_name, constituent_param, constituent_time)
        self.save_alert(deal_with_name)

    def subsection_constituent_system(self, order_start_time, order_end_time, order_peak_width, order_slope
                                      , constituent_name, constituent_param, constituent_time, empty_volume_time,
                                      suitparams_column_length, baseline_noise_max,
                                      baseline_drift_max, baseline_running_time, baseline_start_time,
                                      baseline_end_time, computer_baseline_start_time,
                                      computer_baseline_end_time, pda_slice_width, deal_with_name):
        """
        分段积分 + 组分 + 系统适应性
        :return:
        """
        self.subsection_integration(order_start_time, order_end_time, order_peak_width, order_slope)
        self.constituent(constituent_name, constituent_param, constituent_time)
        self.system_adaptability(empty_volume_time, suitparams_column_length, baseline_noise_max,
                                 baseline_drift_max, baseline_running_time, baseline_start_time,
                                 baseline_end_time, computer_baseline_start_time,
                                 computer_baseline_end_time, pda_slice_width)
        self.save_alert(deal_with_name)

    def subsection_constituent_system_pda(self, order_start_time, order_end_time, order_peak_width, order_slope
                                          , constituent_name, constituent_param, constituent_time, empty_volume_time,
                                          suitparams_column_length, baseline_noise_max,
                                          baseline_drift_max, baseline_running_time, baseline_start_time,
                                          baseline_end_time, computer_baseline_start_time,
                                          computer_baseline_end_time, pda_slice_width, wavelength, wavelength_start,
                                          wavelength_end, spectral_library_name, deal_with_name):
        """
        分段积分 + 组分 + 系统适应性 +  pda
        :return:
        """
        self.subsection_integration(order_start_time, order_end_time, order_peak_width, order_slope)
        self.constituent(constituent_name, constituent_param, constituent_time)
        self.system_adaptability(empty_volume_time, suitparams_column_length, baseline_noise_max,
                                 baseline_drift_max, baseline_running_time, baseline_start_time,
                                 baseline_end_time, computer_baseline_start_time,
                                 computer_baseline_end_time, pda_slice_width)
        self.pda(wavelength, wavelength_start, wavelength_end, spectral_library_name)
        self.save_alert(deal_with_name)
