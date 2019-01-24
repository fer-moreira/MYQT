


























b_pat = '<span style="color:#0984ff;">{0}</span>'
r_pat = '<span style="color:#ff0909;">{0}</span>'
marrom_pat = '<span style="color:#725841;">{0}</span>'



schema = {
'select':b_pat,'from'       :b_pat,'inner'      :b_pat,'join'       :b_pat,'on' :b_pat,
'create':b_pat,'table'      :b_pat,'show'       :b_pat,'update'     :b_pat,'key':b_pat,
'desc'  :b_pat,'as'         :b_pat,'reference'  :b_pat,'foreign'    :b_pat,'use':b_pat,
'limit' :b_pat,'references' :b_pat,'and'        :b_pat,

'collate':b_pat,'smallint'       :b_pat,
'engine' :b_pat,'auto_increment' :b_pat,
'primary':b_pat,'charset'        :b_pat,

'(':b_pat,
')':b_pat,
'=':b_pat,

'smallint'  :r_pat,'unsigned'   :r_pat,
'*'         :r_pat,','          :r_pat,
'innodb'    :r_pat,'not'        :r_pat,
'null'      :r_pat,'varchar'    :r_pat,
'utf8'      :r_pat,

'default'   :r_pat
}