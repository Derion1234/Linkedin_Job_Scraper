def html_gmail(job_obj):
	var_html="""\
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
	<head>
	  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	  <!--[if !mso]><!-->
	  <meta http-equiv="X-UA-Compatible" content="IE=edge">
	  <!--<![endif]-->
	  <meta name="viewport" content="width=device-width, initial-scale=1.0">
	  <meta name="format-detection" content="telephone=no">
	  <meta name="x-apple-disable-message-reformatting">
	  <title></title>
	  <style type="text/css">
	    @media screen {
	      @font-face {
	        font-family: 'Fira Sans';
	        font-style: normal;
	        font-weight: 300;
	        src: local(''),
	        url('https://fonts.gstatic.com/s/firasans/v10/va9B4kDNxMZdWfMOD5VnPKruRA.woff2') format('woff2'),
	        url('https://fonts.gstatic.com/s/firasans/v10/va9B4kDNxMZdWfMOD5VnPKruQg.woff') format('woff');
	      }
	      @font-face {
	        font-family: 'Fira Sans';
	        font-style: normal;
	        font-weight: 400;
	        src: local(''),
	        url('https://fonts.gstatic.com/s/firasans/v10/va9E4kDNxMZdWfMOD5VflQ.woff2') format('woff2'),
	        url('https://fonts.gstatic.com/s/firasans/v10/va9E4kDNxMZdWfMOD5Vfkw.woff') format('woff');
	      }
	      @font-face {
	        font-family: 'Fira Sans';
	        font-style: normal;
	        font-weight: 500;
	        src: local(''),
	        url('https://fonts.gstatic.com/s/firasans/v10/va9B4kDNxMZdWfMOD5VnZKvuRA.woff2') format('woff2'),
	        url('https://fonts.gstatic.com/s/firasans/v10/va9B4kDNxMZdWfMOD5VnZKvuQg.woff') format('woff');
	      }
	      @font-face {
	        font-family: 'Fira Sans';
	        font-style: normal;
	        font-weight: 700;
	        src: local(''),
	        url('https://fonts.gstatic.com/s/firasans/v10/va9B4kDNxMZdWfMOD5VnLK3uRA.woff2') format('woff2'),
	        url('https://fonts.gstatic.com/s/firasans/v10/va9B4kDNxMZdWfMOD5VnLK3uQg.woff') format('woff');
	      }
	      @font-face {
	        font-family: 'Fira Sans';
	        font-style: normal;
	        font-weight: 800;
	        src: local(''),
	        url('https://fonts.gstatic.com/s/firasans/v10/va9B4kDNxMZdWfMOD5VnMK7uRA.woff2') format('woff2'),
	        url('https://fonts.gstatic.com/s/firasans/v10/va9B4kDNxMZdWfMOD5VnMK7uQg.woff') format('woff');
	      }
	    }
	  </style>
	  <style type="text/css">
	    #outlook a {
	      padding: 0;
	    }

	    .ReadMsgBody,
	    .ExternalClass {
	      width: 100%;
	    }

	    .ExternalClass,
	    .ExternalClass p,
	    .ExternalClass td,
	    .ExternalClass div,
	    .ExternalClass span,
	    .ExternalClass font {
	      line-height: 100%;
	    }

	    div[style*="margin: 14px 0"],
	    div[style*="margin: 16px 0"] {
	      margin: 0 !important;
	    }

	    table,
	    td {
	      mso-table-lspace: 0;
	      mso-table-rspace: 0;
	    }

	    table,
	    tr,
	    td {
	      border-collapse: collapse;
	    }

	    body,
	    td,
	    th,
	    p,
	    div,
	    li,
	    a,
	    span {
	      -webkit-text-size-adjust: 100%;
	      -ms-text-size-adjust: 100%;
	      mso-line-height-rule: exactly;
	    }

	    img {
	      border: 0;
	      outline: none;
	      line-height: 100%;
	      text-decoration: none;
	      -ms-interpolation-mode: bicubic;
	    }

	    a[x-apple-data-detectors] {
	      color: inherit !important;
	      text-decoration: none !important;
	    }

	    body {
	      margin: 0;
	      padding: 0;
	      width: 100% !important;
	      -webkit-font-smoothing: antialiased;
	    }

	    .pc-gmail-fix {
	      display: none;
	      display: none !important;
	    }

	    @media screen and (min-width: 621px) {
	      .pc-email-container {
	        width: 620px !important;
	      }
	    }
	  </style>
	  <style type="text/css">
	    @media screen and (max-width:620px) {
	      .pc-sm-p-20 {
	        padding: 20px !important
	      }
	      .pc-sm-p-35-30-40 {
	        padding: 35px 30px 40px !important
	      }
	      .pc-sm-mw-100pc {
	        max-width: 100% !important
	      }
	      .pc-sm-m-0-auto {
	        float: none !important;
	        margin: auto !important
	      }
	    }
	  </style>
	  <style type="text/css">
	    @media screen and (max-width:525px) {
	      .pc-xs-p-10 {
	        padding: 10px !important
	      }
	      .pc-xs-p-20-20-25 {
	        padding: 20px 20px 25px !important
	      }
	      .pc-xs-br-disabled br {
	        display: none !important
	      }
	    }
	  </style>
	  <!--[if mso]>
	    <style type="text/css">
	        .pc-fb-font {
	            font-family: Helvetica, Arial, sans-serif !important;
	        }
	    </style>
	    <![endif]-->
	  <!--[if gte mso 9]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
	</head>
	<body style="width: 100% !important; margin: 0; padding: 0; mso-line-height-rule: exactly; -webkit-font-smoothing: antialiased; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; background-color: #eed2d2" class="">
	  <div style="display: none !important; visibility: hidden; opacity: 0; overflow: hidden; mso-hide: all; height: 0; width: 0; max-height: 0; max-width: 0; font-size: 1px; line-height: 1px; color: #151515;">Nuevo trabajo encontrado!!.</div>
	  <div style="display: none !important; visibility: hidden; opacity: 0; overflow: hidden; mso-hide: all; height: 0; width: 0; max-height: 0; max-width: 0; font-size: 1px; line-height: 1px;">
	    ‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;
	  </div>
	  <table class="pc-email-body" width="100%" bgcolor="#eed2d2" border="0" cellpadding="0" cellspacing="0" role="presentation" style="table-layout: fixed;">
	    <tbody>
	      <tr>
	        <td class="pc-email-body-inner" align="center" valign="top">
	          <!--[if gte mso 9]>
	            <v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
	                <v:fill type="tile" src="" color="#eed2d2"></v:fill>
	            </v:background>
	            <![endif]-->
	          <!--[if (gte mso 9)|(IE)]><table width="620" align="center" border="0" cellspacing="0" cellpadding="0" role="presentation"><tr><td width="620" align="center" valign="top"><![endif]-->
	          <table class="pc-email-container" width="100%" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="margin: 0 auto; max-width: 620px;">
	            <tbody>
	              <tr>
	                <td align="left" valign="top" style="padding: 0 10px;">
	                  <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
	                    <tbody>
	                      <tr>
	                        <td height="20" style="font-size: 1px; line-height: 1px;">&nbsp;</td>
	                      </tr>
	                    </tbody>
	                  </table>
	                  <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
	                    <tbody>
	                      <tr>
	                        <td valign="top">
	                          <!-- BEGIN MODULE: Menu 1 -->
	                          <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
	                            <tbody>
	                              <tr>
	                                <td class="pc-sm-p-20 pc-xs-p-10" bgcolor="#1B1B1B" valign="top" style="padding: 25px 30px; background-color: #A9A9A">
	                                  <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
	                                    <tbody>
	                                      <tr>
	                                        <td align="center" valign="top" style="padding: 10px;">
	                                          <img src="""+job_obj["image_url"]+""" width="130" height="22" alt="" style="height: auto; max-width: 100%; border: 0; line-height: 100%; outline: 0; -ms-interpolation-mode: bicubic; color: #ffffff; font-size: 14px;">
	                                        </td>
	                                      </tr>
	                                      <tr>
	                                        <td align="center" valign="top">
	                                          <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation">
	                                            <tbody>
	                                              <tr>
	                                              </tr>
	                                            </tbody>
	                                          </table>
	                                        </td>
	                                      </tr>
	                                    </tbody>
	                                  </table>
	                                </td>
	                              </tr>
	                            </tbody>
	                          </table>
	                          <!-- END MODULE: Menu 1 -->
	                          <!-- BEGIN MODULE: E-Commerce 1 -->
	                          <table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation">
	                            <tbody>
	                              <tr>
	                                <td class="pc-sm-p-35-30-40 pc-xs-p-20-20-25" valign="top" bgcolor="#ffffff" style="padding: 35px 40px 40px; background-color: #ffffff">
	                                  <table border="0" cellpadding="0" cellspacing="0" width="100%" role="presentation">
	                                    <tbody>
	                                      <tr>
	                                        <td valign="top" align="center" style="padding: 5px 0; font-family: 'Fira Sans', Helvetica, Arial, sans-serif; font-size: 24px; font-weight: 700; line-height: 34px; letter-spacing: -0.4px; color: #151515;">
	                                          Nuevo trabajo!.
	                                        </td>
	                                      </tr>
	                                      <tr>
	                                        <td height="25" style="font-size: 1px; line-height: 1px;">&nbsp;</td>
	                                      </tr>
	                                    </tbody>
	                                    <tbody>
	                                      <tr>
	                                        <td valign="top" align="center">
	                                          <img src="""+job_obj["image_url"]+""" width="384" height="400" alt="" style="border: 0; line-height: 100%; outline: 0; -ms-interpolation-mode: bicubic; display: block; color: #151515; max-width: 100%; height: auto; Margin: 0 auto;">
	                                        </td>
	                                      </tr>
	                                      <tr>
	                                        <td height="15" style="font-size: 1px; line-height: 1px;">&nbsp;</td>
	                                      </tr>
	                                    </tbody>
	                                    <tbody>
	                                      <tr>
	                                        <td class="pc-fb-font" style="font-family: 'Fira Sans', Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 500; color: #40BE65;" valign="top" align="center">
	                                          """+job_obj["company name"]+"""
	                                        </td>
	                                      </tr>
	                                      <tr>
	                                        <td height="8" style="font-size: 1px; line-height: 1px;">&nbsp;</td>
	                                      </tr>
	                                    </tbody>
	                                    <tbody>
	                                      <tr>
	                                        <td class="pc-fb-font" style="font-family: 'Fira Sans', Helvetica, Arial, sans-serif; font-size: 24px; font-weight: 700; line-height: 34px; letter-spacing: -0.4px; color: #151515;" valign="top" align="center">
	                                          """+job_obj["job title"]+"""
	                                        </td>
	                                      </tr>
	                                      <tr>
	                                        <td height="10" style="font-size: 1px; line-height: 1px;">&nbsp;</td>
	                                      </tr>
	                                    </tbody>
	                                    <tbody>
	                                      <tr>
	                                        <td class="pc-fb-font" style="font-family: 'Fira Sans', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 300; line-height: 28px; letter-spacing: -0.2px; color: #9B9B9B;" valign="top" align="center">
	                                          The company <strong>»"""+job_obj["company name"]+"""</strong> is looking for a """+job_obj["job title"]+"""<br> job released at """+job_obj["job_release"]+"""
	                                        </td>
	                                      </tr>
	                                      <tr>
	                                        <td height="20" style="font-size: 1px; line-height: 1px;">&nbsp;</td>
	                                      </tr>
	                                    </tbody>
	                                    <tbody>
	                                      <tr>
	                                        <td height="15" style="font-size: 1px; line-height: 1px;">&nbsp;</td>
	                                      </tr>
	                                    </tbody>
	                                    <tbody>
	                                      <tr>
	                                        <td style="padding-top: 5px" valign="top" align="center">
	                                          <table border="0" cellpadding="0" cellspacing="0" role="presentation">
	                                            <tbody>
	                                              <tr>
	                                                <td style="border-radius: 8px; padding: 13px 17px; background-color: #1595E7;" bgcolor="#1595E7" valign="top" align="center">
	                                                  <a href="""+job_obj["job url"]+""" style="line-height: 24px; text-decoration: none; word-break: break-word; font-weight: 500; display: block; font-family: 'Fira Sans', Helvetica, Arial, sans-serif; font-size: 16px; color: #ffffff;">Postulate ya!</a>
	                                                </td>
	                                              </tr>
	                                            </tbody>
	                                          </table>
	                                        </td>
	                                      </tr>
	                                    </tbody>
	                                  </table>
	                                </td>
	                              </tr>
	                            </tbody>
	                          </table>
	                          <!-- END MODULE: E-Commerce 1 -->
	                        </td>
	                      </tr>
	                    </tbody>
	                  </table>
	                  <table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation">
	                    <tbody>
	                      <tr>
	                        <td height="20" style="font-size: 1px; line-height: 1px;">&nbsp;</td>
	                      </tr>
	                    </tbody>
	                  </table>
	                </td>
	              </tr>
	            </tbody>
	          </table>
	          <!--[if (gte mso 9)|(IE)]></td></tr></table><![endif]-->
	        </td>
	      </tr>
	    </tbody>
	  </table>
	  <!-- Fix for Gmail on iOS -->
	  <div class="pc-gmail-fix" style="white-space: nowrap; font: 15px courier; line-height: 0;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </div>
	</body>
	</html>"""
	return var_html