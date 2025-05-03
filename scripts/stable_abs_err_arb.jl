const EPS = eps(Float64)

function x1_prim(p, q)
    D = p^2 - 4*q
    if D < 0
        return nothing
    end
    -(p + sqrt(D))/2
end
function x1_stab(p, q)
    D = p^2 - 4*q
    if D < 0
        return nothing
    end
    -(p + sqrt(D))/2
end

p = 10 .^ range(;start=1, stop=14.5, length=500)
q = 1.0
X1 = x1_prim.(p, [q]);
X1_st = x1_stab.(p, [q])
X1_t = x1_stab.(BigFloat.(p), [BigFloat(q)])
err_prim = abs.((X1 .- X1_t))
err_stab = abs.((X1_st .- X1_t))


using Plots
pythonplot()
pl = plot(xlabel="p", ylabel="Absoluter Fehler", xaxis=:log, 
#	yaxis=:log
)
plot!(pl, p, err_prim, label="Instabil (float64)")
plot!(pl, p, err_stab, label="Stabil (Vieta, float64)", color=:orange)
#plot!(pl, p, p .* EPS, label="Maschinengenauigkeit mal p", linestyle=:dash, color=:gray)

savefig(pl, "tmp.pdf")
