b_pat       = '<span style="color:#0000ff;">{0}</span>'
r_pat       = '<span style="color:#fc030a;">{0}</span>'
marrom_pat  = '<span style="color:#000000;">{0}</span>'

schema = {
'select':b_pat,'from'       :b_pat,'inner'      :b_pat,'join'       :b_pat,'on' :b_pat,
'create':b_pat,'table'      :b_pat,'show'       :b_pat,'update'     :b_pat,'key':b_pat,
'desc'  :b_pat,'as'         :b_pat,'reference'  :b_pat,'foreign'    :b_pat,'use':b_pat,
'limit' :b_pat,'references' :b_pat,'and'        :b_pat,

'collate':b_pat,'smallint'      :b_pat,
'primary':b_pat,'not'           :b_pat,
'null'   :b_pat,'auto_increment':b_pat,

'charset':'<br></br>%s'%b_pat,
'engine' :'<br></br>%s'%b_pat,

'(':b_pat,
')':b_pat,
'=':b_pat,

'smallint'  :r_pat,'unsigned'   :r_pat,
'*'         :r_pat,','          :r_pat,
'innodb'    :r_pat,'varchar'    :r_pat,
'utf8'      :r_pat,'tinyint'    :r_pat,

'default'   :r_pat
}